Digizilla Odoo 19 Module

Overview:
---------
This is a custom Odoo 19 Community Edition module called "Digizilla".
It implements a new model with related views, menus, reports, and security settings.

Features:
---------
1. Model: digizilla.digizilla
   - Fields: Name*, Gender, Country, Birth Date, Age (computed), Tags, Customers*, No. of Sales Orders, Notes, Comments
   - Required fields are marked with *
2. Views:
   - Form (with Notes and Comments tabs)
   - Kanban
   - List
   - Pivot
3. Menus:
   - Digizilla → Records → Digizilla Records
4. Reports:
   - PDF report including all fields
   - Accessible from form view
5. Security:
   - Restricted to "Digizillians" group
   - Menu visible to users with proper permissions
6. JavaScript:
   - Hides the Create button on the form view (optional)
