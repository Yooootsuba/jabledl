import time
import requests
import threading


class Downloader:

    def __init__(self, segments, request_headers):
        self.threads           = []
        self.threads_count     = 0
        self.threads_limit     = 100

        self.segments          = segments
        self.segments_count    = len(segments)

        self.requests_headers  = request_headers


    def wait_threads(self):
        for thread in self.threads:
            thread.join()

        self.threads_count = 0
        self.threads.clear()


    def thread_job(self, filename, segment):
        try:
            response = requests.get(segment, headers = self.requests_headers)
            with open(filename, 'wb') as f:
                f.write(response.content)

        except:
            time.sleep(5)
            self.thread_job(filename, segment)


    def download(self):
        for i in range(self.segments_count):
            if self.threads_count > self.threads_limit:
                self.wait_threads()

            self.threads.append(threading.Thread(target = self.thread_job, args = (str(i) + '.ts', self.segments[i])))
            self.threads[-1].start()
            self.threads_count += 1

        self.wait_threads()
