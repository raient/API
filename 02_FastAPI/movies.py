from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import nest_asyncio
from pyngrok import ngrok
import uvicorn

def get_movies(rank):
  result = ''
  soup = BeautifulSoup(urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20161120').read(), 'html.parser')
  res = soup.find_all('div', 'tit5')
  for i in range(rank):
    result += "<p>%d - %s\n"%(i+1,res[i].get_text().strip())
  return result

app = FastAPI()

@app.get('/movies/', response_class=HTMLResponse)
async def getMovies(rank:int):
  return get_movies(rank)

ngrok_tunnel = ngrok.connect(8000)
print ('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, host='0.0.0.0', port=8000)
