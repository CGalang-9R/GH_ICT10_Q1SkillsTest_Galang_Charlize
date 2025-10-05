from pyscript import display, document

def order(event=None):
    document.getElementById('details').innerHTML = " "
    info1 = document.getElementById('name').value
    info2 = document.getElementById('address').value
    info3 = document.getElementById('contact').value

    info = f"""
        Order for: {info1}
        Address: {info2}
        Contact number: {info3}
        """

    display(info, target="details")

    document.getElementById('total').textContent = ""
    total = 0
    boxes = document.querySelectorAll('.box')
    for box in boxes:
        if box.checked:
            total += int(box.value)

    info = f'Total: {total}'

    display(info, target="total")