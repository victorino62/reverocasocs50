# **Rever Ocaso - Web Application**
#### Video Demo:  (https://youtu.be/AwPYa7-3_gc)
#### Description:

This is the repository for the **Rever Ocaso** project, a web application developed to promote the artistic concept of the project. The website enables interaction with visitors through features such as a newsletter subscription and a contact form, while also providing access to musical and informational content.

---

## **Technologies Used**

- **Language:** Python
- **Framework:** Flask
- **Front-end:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Development Environment:** VS Code
- **Deployment:** Heroku

---

## **Features**

- **Dynamic Homepage:** Displays information and the concept of the **Rever Ocaso** project.
- **Newsletter Module:** Allows email registration in an SQLite database for future communication.
- **Contact Form:** Processes messages sent by visitors to facilitate communication.
- **Newsletter Management:** Admin page to view registered emails.
- **Static File Monitoring:** Automatic updates for HTML, CSS, and JS files during development.

---

## **How to Run Locally**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rever-ocaso.git
   cd rever-ocaso
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```bash
   python app.py
   ```

5. Open the site in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

## **How to Deploy to Heroku**

1. Make sure the Heroku CLI is installed:
   ```bash
   heroku login
   ```

2. Add the repository to Heroku:
   ```bash
   heroku git:remote -a app-name
   ```

3. Deploy the application:
   ```bash
   git push heroku main
   ```

4. Access the application:
   ```
   https://app-name.herokuapp.com
   ```

---

## **Important Notes**

- When working locally on the project using **VS Code**, make sure to exit Dropbox to avoid file synchronization and permission issues.
- The Flask server must be restarted after changes to the main code to reflect updates.





