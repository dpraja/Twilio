from fpdf import FPDF, HTMLMixin
 
def genpdf(request):
            
    class HTML2PDF(FPDF, HTMLMixin):
        pass

        
    pdf = HTML2PDF()
    name="Customer"
    hotel_name = "Hilton Hotel"
    address = "No:5, First cross street,Chennai-600 001."
    mobile_no = "9677577914"
    email = "abcd96@gmail.com"
    arrival = "2019-05-10"
    departure ="2019-05-15"
    room_type = "Standard Room"
    conf_no = "8974561234"

    pdf.add_page()
    pdf.set_font("Arial",'B', size=16)
    pdf.cell(200, 10, txt="Booking Confirmation", ln=1, align="C")
    pdf.ln(10)
    pdf.set_font('Arial','B',size=14)
    pdf.cell(10)
    pdf.cell(0, 5,"%s," %hotel_name, ln=1, align="L")

    pdf.set_font('Arial','I',size=12)
    pdf.cell(10)
    pdf.cell(0, 5, '%s'%address, ln=1, align="L")
    pdf.cell(10)
    pdf.cell(0, 5, '%s'%mobile_no, ln=1, align="L")
    pdf.cell(10)
    pdf.cell(0, 5, '%s'%email, ln=1, align="L")
    pdf.cell(10)
    pdf.set_font('Arial',size=12)
    pdf.cell(200, 10, txt="Dear %s, " %name, ln=1, align="J")
    pdf.cell(5)
    # Save top coordinate
    top = pdf.y

    # Calculate x position of next cell
    offset = pdf.x + 40
    text_val="""               We are delighted that you have selected our """+hotel_name+""" On behalf of the entire team at the\
     """+hotel_name+""", extend you a very welcome and trust stay with us will be both enjoyable and comfortable\
     """+hotel_name+""" offers a selection of business services and facilities,which are detailed in the booklet\
     placed on the writing table in your room.
                  Should you require any assistance or have any specific\
     requirements,please do not hesitate to contact me extension(999).
    """

    '''
    pdf.multi_cell(180,7,'We are delighted that you have selected our %s On behalf of the entire team at the %s ,\
    extend you a very welcome and trust stay with us will be both enjoyable and comfortable %s offers a selection of business services and facilities,\
    which are detailed in the booklet placed on the writing table in your room.Should you require any assistance or have any specific requirements,\
    please do not hesitate to contact me extension(999)'%(hotel_name,hotel_name,hotel_name),0,0)
    '''

    pdf.cell(5)
    pdf.multi_cell(180,7,text_val,0,0)
    pdf.ln(5)
    pdf.set_text_color(0,0,255)
    pdf.cell(10)
    pdf.cell(0, 5, 'Confirmation Number : %s'%conf_no, ln=1, align="L")
    pdf.cell(10)
    pdf.cell(0, 5, 'Arrival Date : %s'%arrival, ln=1, align="L")
    pdf.cell(10)
    pdf.cell(0, 5, 'Departure Date : %s'%departure, ln=1, align="L")
    pdf.cell(10)
    pdf.cell(0, 5, 'Room Type : %s'%room_type, ln=1, align="L")
    pdf.ln(5)
    pdf.set_text_color(0,0,0)
    pdf.cell(10)
    pdf.cell(0, 5, 'With best regards / Yours sincerely,', ln=1, align="L")
    pdf.set_font('Arial','I',size=12)
    pdf.cell(10)
    pdf.cell(0, 5, 'Hotel Manager', ln=1, align="L")

    pdf.output('uploadpdf/booking_confirmation_pdf_file.pdf','F')

    return json.dumps({"Return":"sucess"})

    
