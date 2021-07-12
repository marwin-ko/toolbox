import multiprocessing as mp


def my_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = round(time.time(),2)
        logger.info("Data Transfer Duration: %s sec", end - start)
        return f
    return wrapper

def download(job):
  bucket, filekey = job
  # some download code
  
@my_timer
def parallel_download(jobs):
  pool = mp.Pool(mp.cpu_count())
  pool.map(download, jobs)
  pool.close()
  pool.join()

def get_jobs(df):
  jobs = list()
  for idx, row in df.iterrows():
    bucket = row.bucket
    filekey = row.rawfile_key
    jobs.append((bucket, filekey))
   return jobs


jobs = get_jobs(df)
parallel_download
