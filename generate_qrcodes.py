# -*- coding: utf-8 -*-
import os

links = {
    'QRCode_CoreiaDoNorte.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/coreia-do-norte/',
    'QRCode_Somalia.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/somalia/',
    'QRCode_Iemen.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/iemen/',
    'QRCode_Sudao.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/sudao/',
    'QRCode_Eritreia.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/eritreia/',
    'QRCode_Siria.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/siria/',
    'QRCode_Nigeria.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/nigeria/',
    'QRCode_Paquistao.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/paquistao/',
    'QRCode_Libia.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/libia/',
    'QRCode_Ira.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/ira/',
    'QRCode_Afeganistao.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/afeganistao/',
    'QRCode_India.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/india/',
    'QRCode_ArabiaSaudita.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/arabia-saudita/',
    'QRCode_Mianmar.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/mianmar/',
    'QRCode_Mali.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/mali/',
    'QRCode_BurkinaFaso.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/burkina-faso/',
    'QRCode_China.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/china/',
    'QRCode_Iraque.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/iraque/',
    'QRCode_Maldivas.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/maldivas/',
    'QRCode_Argelia.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/argelia/',
    'QRCode_Mauritania.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/mauritania/',
    'QRCode_RepCentroAfricana.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/republica-centro-africana/',
    'QRCode_Marrocos.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/marrocos/',
    'QRCode_Cuba.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/cuba/',
    'QRCode_Uzbequistao.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/uzbequistao/',
    'QRCode_Niger.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/niger/',
    'QRCode_Tajiquistao.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/tajiquistao/',
    'QRCode_Laos.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/laos/',
    'QRCode_RepDemDoCongo.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/republica-democratica-do-congo/',
    'QRCode_Mexico.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/mexico/',
    'QRCode_Tunisia.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/tunisia/',
    'QRCode_Nicaragua.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/nicaragua/',
    'QRCode_Bangladesh.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/bangladesh/',
    'QRCode_Butao.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/butao/',
    'QRCode_Turcomenistao.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/turcomenistao/',
    'QRCode_Etiopia.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/etiopia/',
    'QRCode_Camaroes.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/camaroes/',
    'QRCode_Oma.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/oma/',
    'QRCode_Mocambique.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/mocambique/',
    'QRCode_Quirguistao.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/quirguistao/',
    'QRCode_Turquia.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/turquia/',
    'QRCode_Egito.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/egito/',
    'QRCode_Comores.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/comores/',
    'QRCode_Qatar.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/catar/',
    'QRCode_Cazaquistao.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/cazaquistao/',
    'QRCode_Nepal.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/nepal/',
    'QRCode_Colombia.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/colombia/',
    'QRCode_Chade.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/chade/',
    'QRCode_Jordania.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/jordania/',
    'QRCode_Brunei.png': 'https://portasabertas.org.br/lista-mundial-da-perseguicao/brunei/',
}

try:
    import qrcode
except ImportError:
    raise SystemExit('Instale a dependencia com: pip install qrcode[pil]')

output_dir = os.path.join(os.path.dirname(__file__), 'QRCodes')
os.makedirs(output_dir, exist_ok=True)

for filename, url in links.items():
    image = qrcode.make(url)
    image.save(os.path.join(output_dir, filename))

print(f'{len(links)} QR Codes gerados em: {output_dir}')
