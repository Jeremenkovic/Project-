from __future__ import absolute_import
from Project.celery import app
import pandas as pd

@app.task
def process_csv(input_file, output_file):
    chunksize = 10 ** 6
    chunks = []
    for chunk in pd.read_csv(input_file, chunksize=chunksize):
        chunks.append(chunk)
    df = pd.concat(chunks, axis=0)
    df = df.groupby(['Song', 'Date']).sum().reset_index()
    df.to_csv(output_file, index=False)
    return output_file
