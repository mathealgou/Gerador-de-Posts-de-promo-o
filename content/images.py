from html2image import Html2Image
from PIL import Image
class Images:
    def generate_images_from_html(html, css):
        # Generate images
        hti = Html2Image()
            
        hti.screenshot(
        html_str=html, css_str=css,
        save_as='test.png'
        )
        # Convert the png to jpg because Instagram only accepts jpg
        img = Image.open('test.png')
        rgb_img = img.convert('RGB')
        rgb_img.save('test.jpg')