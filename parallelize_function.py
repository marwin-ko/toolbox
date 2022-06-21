import multiprocessing as mp


def download(job):
  bucket, filekey = job
  # some download code
  
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

if __name__ == '__main__':
    jobs = get_jobs(df)
    parallel_download(jobs)
