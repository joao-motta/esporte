{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww18560\viewh12720\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
## Backend (Flask - Python)\
from flask import Flask, render_template, request, jsonify\
from flask_sqlalchemy import SQLAlchemy\
from datetime import datetime\
\
app = Flask(__name__)\
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videos.db'\
db = SQLAlchemy(app)\
\
class Video(db.Model):\
    id = db.Column(db.Integer, primary_key=True)\
    court = db.Column(db.String(50), nullable=False)\
    date_time = db.Column(db.DateTime, nullable=False)\
    url = db.Column(db.String(200), nullable=False)\
\
def video_to_dict(video):\
    return \{"id": video.id, "court": video.court, "dateTime": video.date_time.isoformat(), "url": video.url\}\
\
@app.route("/videos", methods=["GET"])\
def get_videos():\
    court = request.args.get("court")\
    date = request.args.get("date")\
    query = Video.query\
    if court:\
        query = query.filter_by(court=court)\
    if date:\
        date_obj = datetime.strptime(date, "%Y-%m-%d")\
        query = query.filter(db.func.date(Video.date_time) == date_obj.date())\
    videos = query.all()\
    return jsonify([video_to_dict(v) for v in videos])\
\
if __name__ == "__main__":\
    db.create_all()\
    app.run(debug=True)}