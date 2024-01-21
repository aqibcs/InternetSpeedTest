# Import the speedtest module
import speedtest

# Create an instance of the Speedtest class
s = speedtest.Speedtest()

# Print a message indicating that the speed test is in progress
print("Testing...\n")

# Measure download speed in bytes per second and convert to Mbps
downloadSpeed = s.download() / 1048576

# Measure upload speed in bytes per second and convert to Mbps
uploadSpeed = s.upload() / 1048576

# Measure ping (latency) and round the result to the nearest integer
pingResult = round(s.results.ping)

# Print the download speed with two decimal places
print(f"Download speed: {downloadSpeed:.2f} Mbps")

# Print the upload speed with two decimal places
print(f"Upload speed: {uploadSpeed: .2f} Mbps")

# Print the ping result in milliseconds
print(f"Ping: {pingResult} ms")
