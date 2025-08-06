import qrcode as qr
# from PIL import Image
# img = qr.make("https://roadmap.sh/r/data-analysis-databases-backend-with-python")
# img.save("Maged's_roadmap.png")
try:
    qr_target = input("Type Your Link Here => ")
    qr_size = int(input("Type The Size you Need (1 -> 40) : "))
    qr_color = input("Color ? => ")
    qr_background_color = input(" background Color ? => ")
    qr_file_name = input("Type The File Name => ")

    if qr_size > 40:
        raise ValueError("QR SIze Out Of Range")
    else:
        pass

    qrcode = qr.QRCode(version=qr_size, 
                 error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border=4, )
    qrcode.add_data(f"{qr_target}")
    qrcode.make(fit=True)
    img = qrcode.make_image(fill_color=f"{qr_color}", back_color=f"{qr_background_color}")
    img.save(f"{qr_file_name}")
    image = img.save(f"{qr_file_name}.png")
except:
    print("Sorry There Is An Error Generating Your Qr, Make Sure Your Data is Right and Try Again.....")
else:
    print("QR-Code Generated Successfully :)")
finally:
    print("Thanks For Using Our Service")

# Description:
# here is the normal logitsic code in a normal or medium level syntax without interface
