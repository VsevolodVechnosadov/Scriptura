from parserer_ii import download_images
from creatoror import create_dir
from converterer import convert_pdf


convert_pdf(download_images(create_dir('https://lib-fond.ru/lib-rgb/210/f-210-22/'), 'https://lib-fond.ru/lib-rgb/210/f-210-22/'))

