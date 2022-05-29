from django.shortcuts import render,redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
client = MongoClient('localhost',27017)

db = client.police_username
posts = db.posts
un = ''
pwd = ''
# Create your views here.
def loginpage(request):
    global un ,pwd
    if request.method =="POST":
    
        res = posts.find({'Name':un})
        if res!=None:
            return redirect('http://127.0.0.1:8000/imageupload')
    return render(request, 'loginpage.html')
