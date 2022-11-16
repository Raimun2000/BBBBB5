# -*- coding: utf-8 *-* 

# IMPORTAMOS LAS LIBRERIAS NECESARIAS
from bs4 import BeautifulSoup
import re
import requests

def Scraper(ruta, rangoPaginas):
      linksPaginas = []      
      for x in rangoPaginas:
            websiteLibro = ruta+'/?p='+str(x)
            result = requests.get(websiteLibro)
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            enlaces = soup.find_all(class_="image-photo")
            links = [x.get('href') for x in enlaces]
            linksPaginas += links
      return linksPaginas

def fListaDeValores(website):
      
      # Obtenemos la SOPA de la página actual.
      soup = fRecorreLibros(website)
      
      ##############################################################
      # EJECUCION DE FUNCIONES PARA OBTENER VALORES DE CADA PAGINA #
      ##############################################################
      
      titulo = fTitulo(soup)
      if titulo == None:
            titulo = "No informado." 
      else:
            titulo = titulo.replace("\n"," ")
            titulo = titulo.replace("\t"," ")
            titulo = titulo.replace("\r"," ")
            titulo = titulo.replace("'"," ")
            titulo = titulo.replace(";"," ")
            titulo = titulo.replace("`"," ")
            titulo = titulo.replace("\""," ")   

      autor = fAutor(soup)
      if autor == None:
            autor = "No informado."
      else:
            autor = autor.replace("\n"," ")
            autor = autor.replace("\t"," ")
            autor = autor.replace("\r"," ")
            autor = autor.replace("'"," ")
            autor = autor.replace(";"," ")
            autor = autor.replace("`"," ")
            autor = autor.replace("\""," ")
            
      dispo = fDispo(soup)
      if dispo == None:
            dispo = "No informado."    
            
      precio = fPrecio(soup)            
      if precio == None:
            precio = "No informado."    


      editorial = fEditorial(soup)
      if editorial == None:
            editorial = "No informada."
      else:
            editorial = editorial.replace("\n"," ")
            editorial = editorial.replace("\t"," ")
            editorial = editorial.replace("\r"," ")
            editorial = editorial.replace("'"," ")
            editorial = editorial.replace(";"," ")
            editorial = editorial.replace("`"," ")
            editorial = editorial.replace("\""," ")

      isbn = fISBN(soup)
      if isbn == None:
            isbn = "No informado."
            
      paginas = fPaginas(soup)
      if paginas == None:
            paginas = "No informado."

      idioma = fIdioma(soup)
      if idioma == None:
            idioma = "No informado."

      formato = fFormato(soup)
      if formato == None:
            formato = "No informado."

      fechaPub = fFechaPublicacion(soup)
      if fechaPub == None:
            fechaPub = "No informado."

      sinopsis = fSinopsis(soup)
      if sinopsis == None:
            sinopsis = "No informado."
      else:
            sinopsis = sinopsis.replace("\n"," ")
            sinopsis = sinopsis.replace("\t"," ")
            sinopsis = sinopsis.replace("\r"," ")
            sinopsis = sinopsis.replace("'"," ")
            sinopsis = sinopsis.replace(";"," ")
            sinopsis = sinopsis.replace("`"," ")
            sinopsis = sinopsis.replace("\""," ")

      biografia = fBiografia(soup)
      if biografia == None:
            biografia = "No informado."
      else:
            biografia = biografia.replace("\n"," ")
            biografia = biografia.replace("\t"," ")
            biografia = biografia.replace("\r"," ")
            biografia = biografia.replace("'"," ")
            biografia = biografia.replace(";"," ")
            biografia = biografia.replace("`"," ")
            biografia = biografia.replace("\""," ")

      clasif = fClasif(soup)
      if clasif == None:
            clasif = "No informado."
      else:
            clasif = clasif.replace("\n"," ")
            clasif = clasif.replace("\t"," ")
            clasif = clasif.replace("\r"," ")
            clasif = clasif.replace("'"," ")
            clasif = clasif.replace(";"," ")
            clasif = clasif.replace("`"," ")
            clasif = clasif.replace("\""," ")
            
      urlImagen = fUrlImagen(soup)

      # Unimos todos los valores reunidos en una lista.
      listaValores = [titulo, autor, dispo, str(precio), editorial, isbn, paginas, idioma, formato, clasif, fechaPub, sinopsis, urlImagen, website]
      
      return listaValores, biografia


# FECHA DE PUBLICACIÓN:
def fFechaPublicacion(soup):
      for div in soup.find_all("div", class_="std"):
            for strong in div.find_all("strong"):
                  pat = re.compile("[0-9][0-9][/][0-9][0-9][0-9][0-9]")
                  fechaPub = strong.text
                  okis = bool(pat.search(fechaPub))
                  if okis == True:                              
                        return fechaPub.strip()

# EDITORIAL:
def fEditorial(soup):
      for div in soup.find_all("div", class_="std"):
            #print(div)
            pat = re.compile("[E][d][i][t][o][r][i][a][l]*")
            editorial = div.text
            okis = bool(pat.search(editorial))
            if okis == True:                   
                  for strong in div.find_all("strong"):
                        editorial = strong.text
                        return editorial.strip()

# ISBN:
def fISBN(soup):
      for div in soup.find_all("div", class_="std"):
            #print(div)
            pat = re.compile("[I][.][S][.][B][.][N]*")
            isbn = div.text
            okis = bool(pat.search(isbn))
            if okis == True:                   
                  for strong in div.find_all("strong"):
                        isbn = strong.text
                        return isbn.strip()

# PAGINAS:      
def fPaginas(soup):
      for div in soup.find_all("div", class_="std"):
            # Nro. de Paginas:
            pat = re.compile("[N][r][o][.]*")
            paginas = div.text
            okis = bool(pat.search(paginas))
            if okis == True:                   
                  for strong in div.find_all("strong"):
                        paginas = strong.text
                        return paginas.strip()

# IDIOMA::      
def fIdioma(soup):
      for div in soup.find_all("div", class_="std"):
            pat = re.compile("[I][d][i][o][m][a][.]*")
            idioma = div.text
            okis = bool(pat.search(idioma))
            if okis == True:                   
                  for strong in div.find_all("strong"):
                        idioma = strong.text
                        return idioma.strip()

# FORMATO:      
def fFormato(soup):
      for div in soup.find_all("div", class_="std"):
            pat = re.compile("[F][o][r][m][a][t][o]*") 
            formato = div.text
            okis = bool(pat.search(formato))
            if okis == True:                   
                  for strong in div.find_all("strong"):
                        formato = strong.text
                        return formato.strip()

# SINOPSIS:      
def fSinopsis(soup):
      sinopsis = soup.find("div", id="ja-tabitem-desc").get_text(strip = True)
      return sinopsis.strip()

# BIOGRAFIA
def fBiografia(soup):
      biografia = soup.find("div", id="ja-tabitem-bio").get_text(strip = True)
      return biografia.strip()

# urlImagen:      
def fUrlImagen(soup):
      urlImagen = soup.find("img", id="main-image")["src"]
      return urlImagen.strip()

# CLASIFICACION::      
def fClasif(soup):
      lista = ""
      esp = " "
      for div in soup.find_all("div", class_="std"):
            pat = re.compile("[C][l][a][s][i][f][i][c][a][c][i]*") # Clasificación:
            clasif = div.text
            okis = bool(pat.search(clasif))
            if okis == True:  
                  for strong in div.find_all("strong"): 
                        for span in strong.find_all("span"):
                              for a in span.find_all("a"):
                                    lista = lista+esp+a.text
                  lista = lista.replace("Libros ","")
                  return lista.strip()

# TITULO:
def fTitulo(soup):      
      titulo = soup.find("div", class_="product-shop").find("h1").get_text(strip=True)
      return titulo

# AUTOR:
def fAutor(soup):
      autor = soup.find("div", class_="product-shop").find("div", class_="author").get_text(strip=True)
      autor = autor.replace("Autor:","")
      return autor

# DISPONIBILIDAD:
def fDispo(soup):
      dispo = soup.find("div", class_="product-shop").find("p",class_="availability in-stock").get_text(strip=True)
      dispo = dispo.replace("Disponibilidad:","")
      return dispo

# PRECIO:
def fPrecio(soup):
      precio = soup.find("div", class_="product-shop").find("span",class_="price").get_text(strip=True)
      precio = precio.replace("$","")
      precio = precio.replace(".","")
      precio = precio.replace(",",".")
      precio = float(precio)
      return precio

# RECORREDOR DE LIBROS 
def fRecorreLibros(website):
      result = requests.get(website)
      content = result.text
      soup = BeautifulSoup(content, 'lxml')
      return soup
