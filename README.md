# Pyinstaller-example

To better understand this example please refer to my [blog post](http://3.120.248.248/?page_id=287)

Plase make sure you have pyinstaller installed.
```
pip install pyinstaller
```
To create a one file executable run the following command:
```
pyinstaller --onefile tkinter_sample_app.py  
```
For more advanced options it's recommended to use .spec file, attached an example of a spec file sample.spec. To create an executable using a spec command:
```
pyinstaller your_app_name.spec
```
You can also refer to this [blog post](http://3.120.248.248/?page_id=295) for more details.
