{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 ## Frontend (React - JavaScript)\
import React, \{ useState, useEffect \} from "react";\
import \{ BrowserRouter as Router, Route, Routes \} from "react-router-dom";\
import \{ Card, CardContent \} from "@/components/ui/card";\
import \{ Button \} from "@/components/ui/button";\
import \{ format \} from "date-fns";\
\
const courts = ["Quadra 1", "Quadra 2", "Quadra 3", "Quadra 4"];\
\
const VideoList = () => \{\
  const [selectedCourt, setSelectedCourt] = useState("Quadra 1");\
  const [date, setDate] = useState("");\
  const [videos, setVideos] = useState([]);\
\
  useEffect(() => \{\
    fetch(`/videos?court=$\{selectedCourt\}&date=$\{date\}`)\
      .then(res => res.json())\
      .then(data => setVideos(data));\
  \}, [selectedCourt, date]);\
\
  return (\
    <div className="p-4">\
      <h1 className="text-xl font-bold">V\'eddeos da \{selectedCourt\}</h1>\
      <div className="flex gap-2 my-2">\
        \{courts.map(court => (\
          <Button key=\{court\} onClick=\{() => setSelectedCourt(court)\}>\
            \{court\}\
          </Button>\
        ))\}\
      </div>\
      <input\
        type="date"\
        value=\{date\}\
        onChange=\{(e) => setDate(e.target.value)\}\
        className="border p-2 rounded mb-4"\
      />\
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">\
        \{videos.map(video => (\
          <Card key=\{video.id\}>\
            <CardContent>\
              <video controls className="w-full">\
                <source src=\{video.url\} type="video/mp4" />\
              </video>\
              <p className="text-sm mt-2">\{format(new Date(video.dateTime), "dd/MM/yyyy HH:mm")\}</p>\
            </CardContent>\
          </Card>\
        ))\}\
      </div>\
    </div>\
  );\
\};\
\
const App = () => \{\
  return (\
    <Router>\
      <div className="p-4">\
        <h1 className="text-2xl font-bold">Plataforma de V\'eddeos Esportivos</h1>\
        <Routes>\
          <Route path="/" element=\{<VideoList />\} />\
        </Routes>\
      </div>\
    </Router>\
  );\
\};\
\
export default App;}