import json
import random
import time
import requests


class OrbitionMasterBot:

  def __init__(self, bearer_token, ua_file="user-agent.txt"):
    self.base_url = "https://api-airdrop.orbition.network"
    self.bearer_token = bearer_token.strip()
    self.user_agents = self.muat_user_agents(ua_file)

  def muat_user_agents(self, filepath):
    try:
      with open(filepath, "r", encoding="utf-8") as f:
        uas = [line.strip() for line in f if line.strip()]
        if uas:
          return uas
    except FileNotFoundError:
      pass
    return [
        (
            "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like"
            " Gecko) Chrome/127.0.0.0 Mobile Safari/537.36"
        )
    ]

  def buat_session_baru(self):
    session = requests.Session()
    chosen_ua = random.choice(self.user_agents)
    session.headers.update({
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "id-ID",
        "Authorization": f"Bearer {self.bearer_token}",
        "Content-Type": "application/json",
        "Origin": "https://airdrop.orbition.network",
        "Referer": "https://airdrop.orbition.network/",
        "User-Agent": chosen_ua,
    })
    return session

  def cek_profil(self):
    session = self.buat_session_baru()
    try:
      response = session.get(f"{self.base_url}/api/me")
      if response.status_code == 200:
        data = response.json()
        user_data = data.get("user", data)
        total_obn = float(user_data.get("total_points", 0))
        wallet = user_data.get("wallet_address", "Belum")
        mining_status = user_data.get("mining_status")

        print(f"💰 Total OBN       : {total_obn}")
        print(f"👛 Wallet Address  : {wallet}")
        print(f"⛏️  Mining Status   : {mining_status}")
        return total_obn
      else:
        print(f"[-] Gagal mengambil profil: {response.status_code}")
    except Exception as e:
      print(f"[!] Error: {e}")
    return 0.0

  def start_mining(self):
    session = self.buat_session_baru()
    try:
      print("\n[*] Menjalankan Mining...")
      response = session.post(f"{self.base_url}/api/mining/start", json={})
      if response.status_code == 200:
        print(f"[+] Berhasil memulai AI Mining! Respon: {response.text}")
      else:
        print(f"[-] Gagal start mining: {response.status_code}")
    except Exception as e:
      print(f"[!] Error: {e}")

  def cek_dan_proses_quest(self):
    session = self.buat_session_baru()
    try:
      print("\n[*] Mengecek Quest yang Belum Selesai...")
      response = session.get(f"{self.base_url}/api/quests")
      if response.status_code != 200:
        print(f"[-] Gagal mengambil quest: {response.status_code}")
        return

      data = response.json()
      quests = data.get("quests", data) if isinstance(data, dict) else data
      if not isinstance(quests, list):
        return

      quest_belum_selesai = [
          q for q in quests if not q.get("completed", False)
      ]
      if not quest_belum_selesai:
        print("[+] Semua quest pada akun ini sudah selesai dikerjakan!")
        return

      print(f"[+] Ditemukan {len(quest_belum_selesai)} quest aktif.\n" + "-" * 50)
      for idx, quest in enumerate(quest_belum_selesai, 1):
        quest_id = quest.get("id") or quest.get("questId")
        title = quest.get("title", "Tanpa Judul")
        print(
            f"[{idx}] ID: {quest_id} | Judul: {title} | Reward OBN:"
            f" {quest.get('reward', 'N/A')}"
        )
        if quest_id:
          self.verifikasi_quest(quest_id)
          time.sleep(2)
        print("-" * 50)
    except Exception as e:
      print(f"[!] Error: {e}")

  def verifikasi_quest(self, quest_id):
    session = self.buat_session_baru()
    try:
      response = session.post(
          f"{self.base_url}/api/quests/verify", json={"questId": quest_id}
      )
      if response.status_code == 200:
        print(f"    └─ [+] Berhasil! Respon: {response.text}")
      else:
        print(f"    └─ [-] Gagal: {response.text}")
    except Exception as e:
      print(f"    └─ [!] Error: {e}")


def muat_daftar_token(filepath="token.txt"):
  try:
    with open(filepath, "r", encoding="utf-8") as f:
      tokens = [line.strip() for line in f if line.strip()]
      return tokens
  except FileNotFoundError:
    print(f"[-] File '{filepath}' tidak ditemukan!")
    return []


if __name__ == "__main__":
  tokens = muat_daftar_token("token.txt")

  if not tokens:
    print("[-] Tidak ada token yang dimuat. Pastikan file token.txt terisi.")
    exit()

  print(f"[+] Berhasil memuat {len(tokens)} akun dari token.txt\n")

  while True:
    print("=" * 35)
    print("      MENU UTAMA MULTI-AKUN")
    print("=" * 35)
    print("1. Cek Profile & Total OBN (Semua Akun)")
    print("2. Start Mining (Semua Akun)")
    print("3. Cek & Kerjakan Quest (Semua Akun)")
    print("4. Kerjakan Quest & Start Mining (Gabungan - Semua Akun)")
    print("5. Jalankan Semua Sekaligus (Semua Akun)")
    print("6. Keluar")
    print("=" * 35)

    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "6":
      print("[+] Keluar program. Sampai jumpa!")
      break

    if pilihan not in ["1", "2", "3", "4", "5"]:
      print("[-] Pilihan tidak valid.")
      continue

    # Variabel penampung total keseluruhan OBN khusus untuk menu 1
    grand_total_obn = 0.0

    for i, token in enumerate(tokens, 1):
      print(f"\n" + "#" * 50)
      print(f" >>> MEMPROSES AKUN KE-{i} dari {len(tokens)}")
      print("#" * 50)

      bot = OrbitionMasterBot(bearer_token=token, ua_file="user-agent.txt")

      if pilihan == "1":
        print("\n[*] Mengecek Profil & Saldo OBN...")
        print("=" * 45)
        print(f"          STATUS AKUN ORBITION #{i}")
        print("=" * 45)
        poin_akun = bot.cek_profil()
        print("=" * 45)
        grand_total_obn += poin_akun
      elif pilihan == "2":
        bot.start_mining()
      elif pilihan == "3":
        bot.cek_dan_proses_quest()
      elif pilihan == "4":
        bot.cek_dan_proses_quest()
        bot.start_mining()
      elif pilihan == "5":
        print("\n[*] Mengecek Profil...")
        bot.cek_profil()
        bot.start_mining()
        bot.cek_dan_proses_quest()

      print(f"\n[+] Selesai memproses Akun ke-{i}\n" + "=" * 50)
      time.sleep(1)

    # Menampilkan hasil akumulasi total OBN jika memilih menu 1
    if pilihan == "1":
      print("\n" + "=" * 50)
      print(f" 🎯 RINGKASAN TOTAL OBN DARI {len(tokens)} AKUN:")
      print(f" 💰 Grand Total Saldo OBN : {grand_total_obn}")
      print("=" * 50 + "\n")
