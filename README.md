# Custom Invoice Columns – Odoo Module

## 📌 Purpose

This custom module extends Odoo’s Accounting module by adding three additional columns to the customer invoice line:

- **Previous** – last meter reading from the client's previous invoice
- **New** – new meter reading for the current invoice
- **Actual** – the difference between New and Previous readings  
- The **Quantity** field is auto-filled with the Actual value

This is useful for businesses that bill based on meter usage, like utilities.

---

## 🛠️ Installation & Testing Steps

1. **Move the module folder** `custom_invoice_columns/` into your Odoo `addons/` directory
2. **Restart Odoo** to load the new module
3. Open your browser and:
   - Go to **Apps**
   - Activate **Developer Mode** (from Settings > Activate Developer Mode)
   - Click the **3-dot menu** > **Update App List**
   - Search for **Custom Invoice Columns**
   - Click **Install**
4. Create or open a customer invoice under Accounting > Customers > Invoices
5. Add an invoice line to see the new columns (`Previous`, `New`, `Actual`, etc.)
6. Post the invoice to store readings and auto-calculate fields

---

## ⚙️ Dependencies
- Tested on **Odoo 16**
- Should work on **Odoo 14 to 17**
- ⚠️ Compatibility with **Odoo 18** not fully tested yet (may require slight changes)


- Requires the built-in `account` module
- Tested on **Odoo 16** (should work on Odoo 14–17)
- No external libraries or configuration needed

---

## 🔗 GitHub Repository

You can find the complete source code here:  
👉 **[https://github.com/sheriff254-del/custom_invoice_columns](https://github.com/sheriff254-del/custom_invoice_columns)**


---

## ✅ Notes

- Follows Odoo modular design best practices
- Comments and clean code included for clarity
- You can freely extend the module further if needed
