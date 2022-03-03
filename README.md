# Django Tailwind Boilerplate
A repo with the necessary boilerplate to run Django with TailwindCSS without Node.
You can find a detailed description to set this up by yourself on [this blog post](ericluna.dev/blog).

## Instalation
### - Download the Standalone CLI:
Grab the executable for your platform from the [latest release](https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.0.23) on GitHub, making sure to give it executable permissions.

``` bash
# Example for macOS arm64
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-arm64
chmod +x tailwindcss-macos-arm64
mv tailwindcss-macos-arm64 tailwindcss
```

### - Run the watcher
``` bash
./tailwindcss -i static/css/input.css -o static/css/output.css --watch
```

### - Run Django's server
``` bash
# Create a virtualenv
pip install virtualenv
virtualenv .env --python /path/to/python3

# Enable environment
source .env/bin/activate

# Instal dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver
```

## Usage
Just add Tailwind's utility classes to your HTML class attribute.
``` html
<div class="text-3xl text-blue-700 p-8 bg-[#FFCCAA]">Hello World!</div>
```

Changes will update instantly thanks to [django_browser_reload](https://github.com/adamchainz/django-browser-reload).

## Production
When you're ready to deploy your site to production, run the following command for a more optimized css file:
``` bash
./tailwindcss -i static/css/input.css -o static/css/output.css --minify
```
