import os
import glob

def generate_html():
    font_dir = 'fonts'  # Directory where your fonts will be stored
    html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Font Showcase</title>
    <style>
        body {
            font-size: 18px;
            line-height: 1.6;
            font-family: Arial, sans-serif;
        }
        .font-example {
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ddd;
        }
        @font-face {
            font-family: '${font_name}';
            src: url('${font_file}') format('truetype');
        }
    </style>
</head>
<body>
    <h1>Font Showcase</h1>
'''

    for font_file in glob.glob(f'{font_dir}/*.ttf') + glob.glob(f'{font_dir}/*.otf'):
        font_name = os.path.splitext(os.path.basename(font_file))[0]
        html += f'''
    <div class="font-example">
        <h2>{font_name}</h2>
        <p style="font-family: '{font_name}';">The quick brown fox jumps over the lazy dog.</p>
    </div>
        '''

    html += '''
</body>
</html>
'''

    with open('index.html', 'w') as f:
        f.write(html)

if __name__ == "__main__":
    generate_html()