#!/usr/bin/python

import speedtest
import time
from prometheus_client import start_http_server, Summary, Gauge

servers = []
# If you want to test against a specific server
# servers = [1234]

s = speedtest.Speedtest()

#results_dict = s.results.dict()
#print results_dict

g_speed = Gauge('speedtest_bits_per_second', 'Speedtest speed in bits per second.', ['direction'])
g_ping = Gauge('speedtest_latency_ms', 'Speedtest latency in ms.')

# Initialize with 0
g_speed.labels('downstream').set(0.0)
g_speed.labels('upstream').set(0.0)
g_ping.set(0.0)

def process_request(t):
  s.get_servers(servers)
  s.get_best_server()
  s.download()
  s.upload()
  results_dict = s.results.dict()
  g_speed.labels('downstream').set(results_dict["download"])
  g_speed.labels('upstream').set(results_dict["upload"])
  g_ping.set(results_dict["ping"])
  print results_dict["ping"]
  print results_dict["upload"]
  print results_dict["download"]
  time.sleep(t)
  
if __name__ == '__main__':
  # Start up the server to expose the metrics.
  start_http_server(9104) 
  # Generate some requests.
  while True:
    process_request(60)
