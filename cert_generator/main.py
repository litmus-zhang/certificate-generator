import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import io
from send_mail import Mailer


def add_text_to_image(image, fullname, track=None):
    draw = ImageDraw.Draw(image)
    fullname_font = ImageFont.load_default(size=60)
    track_font = ImageFont.load_default(size=30)
    image_width, image_height = image.size
    text_length = draw.textlength(fullname, fullname_font)
    name_position = (image_width - text_length) / 2, (image_height / 2) - 60
    track_position = (image_width / 2) - (text_length / 5), (image_height / 2) + 120
    draw.text(
        name_position,
        text=fullname,
        font=fullname_font,
        fill=(255, 255, 255),
        align="left",
    )
    draw.text(
        track_position,
        text=track,
        font=track_font,
        fill=(0, 0, 0),
        align="center",
    )
    return image


def upload_recipient():
    attendees_list = st.file_uploader("Enter the attendees list:", type=["csv", "xlsx"])
    # attendees_list = pd.read_csv(attendees_list)
    form_response = None
    if attendees_list:
        if attendees_list.name.endswith(".csv"):
            attendees_list = pd.read_csv(attendees_list)
            st.write(attendees_list)
        else:
            sheets = pd.read_excel(attendees_list, sheet_name=None)
            # get the first sheet

            for sheet_name, df in sheets.items():
                if "Form Response" in sheet_name:
                    st.write(f"{sheet_name}")
                    form_response = df
                    st.write(form_response)

            # get the dataframe
            # for each row, get the column with the full name,
            # then replace the placeholder on the template with the image


def main():
    st.title("Certificate Generator")
    st.write("This is a simple certificate generator app.")

    template = st.file_uploader(
        "Upload the certificate template:", type=["jpg", "png", "jpeg"]
    )
    category = st.selectbox(
        "Choose Track", ["FLL/Pictoblox", "FTC", "Drone Tech", "Volunteers"]
    )
    if template is not None:
        image = Image.open(template)
        st.image(image, caption="Original Image")

        fullname = st.text_input("Enter fullname:")
        track = category

        if fullname and track:
            modified_image = add_text_to_image(image, fullname, track=track)
            st.image(modified_image, caption="Modified Image")
            # download the modified image as pdf
            pdf_bytes = io.BytesIO()
            modified_image.save(pdf_bytes, format="PDF")
            pdf_bytes.seek(0)
            st.download_button(
                "Download Now",
                data=pdf_bytes,
                file_name=f"{fullname}.pdf",
                mime="application/pdf",
            )

    upload_recipient()
    mailer = Mailer()
    print(f"{str(mailer)}")


if __name__ == "__main__":
    main()
