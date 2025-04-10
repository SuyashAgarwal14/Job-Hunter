from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'New York, USA',
        'salary': '70,000'
    },

    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'San Francisco, USA',
        'salary': '120,000'
    },

    {
        'id': 3,
        'title': 'Web Developer',
        'location': 'London, UK',
        'salary': '80,000'
    },

    {
        'id': 4,
        'title': 'Software Engineer',
        'location': 'Berlin, Germany',
        'salary': '100,000'
    },

    {
        'id': 5,
        'title': 'Product Manager',
        'location': 'Toronto, Canada',
        'salary': '90,000'
    },

    {
        'id': 6,
        'title': 'UX Designer',
        'location': 'Sydney, Australia',
        'salary': '75,000'
    }
]

@app.route('/')
def home():
    return render_template('home.html', jobs = JOBS, company_name = 'Jovian')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = False, port = 5000)
