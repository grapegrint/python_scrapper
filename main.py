# from bs4 import BeautifulSoup
# import requests
# from extractor.rmtok import extract_rmtok_jobs
# from extractor.wwr import extract_wwr_jobs
# from file import save_to_file

# keyword = input("what areas are you in looking for jobs?\n")
# wwr_jobs = extract_wwr_jobs(keyword)
# rmtok_jobs = extract_rmtok_jobs(keyword)
# jobs = wwr_jobs + rmtok_jobs
# save_to_file(keyword,jobs)


from flask import Flask, render_template, request, redirect
from extractor.rmtok import extract_rmtok_jobs
from extractor.wwr import extract_wwr_jobs


app=Flask("JobScrapper")

@app.route("/") #decorating
def home():
  return render_template("home.html", name="Sinae")

@app.route("/search")
def search():
    keyword=request.args.get("keyword")
    if keyword == None:
      return redirect("/")
    rmtok=extract_rmtok_jobs(keyword)
    wwr=extract_wwr_jobs(keyword)
    jobs= rmtok+ wwr
     
    return render_template("search.html",keyword=keyword, jobs=jobs)
  
  
app.run("0.0.0.0")