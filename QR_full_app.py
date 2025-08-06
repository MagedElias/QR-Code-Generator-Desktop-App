import qrcode
import customtkinter as ctk
from tkinter import messagebox
# Configure customtkinter
ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Theme options: blue, dark-blue, green

# Main QR Code generator function
def generate_qr():
    try:
        qr_target = entry_link.get()
        qr_size = int(entry_size.get())
        qr_color = entry_color.get()
        qr_background_color = entry_bg_color.get()
        qr_file_name = entry_filename.get()

        if not qr_target or not qr_file_name:
            raise ValueError("Link and file name must not be empty")

        if not (1 <= qr_size <= 40):
            raise ValueError("QR size must be between 1 and 40")

        qrcode_obj = qrcode.QRCode(
            version=qr_size,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qrcode_obj.add_data(qr_target)
        qrcode_obj.make(fit=True)
        img = qrcode_obj.make_image(fill_color=qr_color, back_color=qr_background_color)
        img.save(f"{qr_file_name}.png")

        messagebox.showinfo("Success", f"QR Code saved as {qr_file_name}.png")
    except Exception as e:
        messagebox.showerror("Error", f"Error generating QR Code:\n{str(e)}")




# --- By Ai ---
# GUI Setup
app = ctk.CTk()
app.title("Modern QR Code Generator")
app.geometry("500x400")

# Widgets
ctk.CTkLabel(app, text="QR Code Generator", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=15)

entry_link = ctk.CTkEntry(app, placeholder_text="Enter your link here", width=400)
entry_link.pack(pady=8)

entry_size = ctk.CTkEntry(app, placeholder_text="Enter size (1 - 40)", width=400)
entry_size.insert(0, "4")
entry_size.pack(pady=8)

entry_color = ctk.CTkEntry(app, placeholder_text="QR Color (e.g. black)", width=400)
entry_color.insert(0, "black")
entry_color.pack(pady=8)

entry_bg_color = ctk.CTkEntry(app, placeholder_text="Background Color (e.g. white)", width=400)
entry_bg_color.insert(0, "white")
entry_bg_color.pack(pady=8)

entry_filename = ctk.CTkEntry(app, placeholder_text="File name to save as (no extension)", width=400)
entry_filename.insert(0, "my_qr_code")
entry_filename.pack(pady=8)

ctk.CTkButton(app, text="Generate QR Code", command=generate_qr).pack(pady=20)

app.mainloop()



