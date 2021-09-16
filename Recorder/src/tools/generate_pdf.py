import pdfkit

def generate_orders_html():
    pass

def generate_payment_list_html():
    pass

def generate_products_list_html():
    pass

def generate_orders_pdf():
    html = generate_orders_html()
    pdfkit.from_string(html,output_path="tmp/pedidos.pdf")

def generate_payment_list_pdf():
    html = generate_payment_list_html()
    pdfkit.from_string(html,output_path="tmp/cobranza.pdf")

def generate_products_list_pdf():
    html = generate_products_list_html()
    pdfkit.from_string(html,output_path="tmp/despacho.pdf")
