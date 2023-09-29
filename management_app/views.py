from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import Order
from django.shortcuts import get_object_or_404

def some_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    
    # Draw the title on the PDF.
    p.setFont("Helvetica-Bold", 24)  # Set the font to Helvetica, bold, size 24.
    p.drawString(100, 800, f"Order Details #{order_id}")  # Adjust coordinates as necessary.

    # Reset the font.
    p.setFont("Helvetica", 12)

    # Draw order details on the PDF.
    p.drawString(100, 750, f"Order Name: {order.name}")
    p.drawString(100, 730, f"Customer: {order.customer}")
    p.drawString(100, 710, f"Total Hours: {order.total_hours()}")

    p.setFont("Helvetica-Bold", 12) 
    p.drawString(100, 650, "Jobs")

    p.setFont("Helvetica", 12)
    # Iterate through associated jobs and write their details into the PDF.
    y_position = 610
    for job in order.jobs.all():
        p.drawString(100, y_position, f"Job Date: {job.date}")
        p.drawString(100, y_position - 20, f"Job Hours: {job.hours}")
        p.drawString(100, y_position - 40, f"Job Description: {job.description}")
        y_position -= 80  # Adjusts the y_position for the next job.

    p.setFont("Helvetica-Bold", 12) 
    total_hours = order.total_hours()
    p.drawString(100, y_position, f"Total Hours: {total_hours}")

    # Close the PDF object cleanly and ensure it's written to the buffer.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'order_{order_id}_{order.customer}_details.pdf')