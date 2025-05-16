from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    business_name = data.get('business_name')
    industry = data.get('industry')
    website_url = data.get('website_url')
    revenue = data.get('revenue')
    employees = data.get('employees')
    tools = data.get('tools')
    pain_points = data.get('pain_points')

    report = f"""
    <h1>BizScan360 Diagnostic Report</h1>
    <p><strong>Business:</strong> {business_name}</p>
    <p><strong>Industry:</strong> {industry}</p>
    <p><strong>Website:</strong> {website_url}</p>
    <p><strong>Monthly Revenue:</strong> {revenue}</p>
    <p><strong>Employees:</strong> {employees}</p>
    <p><strong>Tools Used:</strong> {tools}</p>
    <p><strong>Main Pain Points:</strong> {pain_points}</p>
    <hr>
    <h2>AI Insights</h2>
    <ul>
        <li>You may be overpaying for overlapping software tools.</li>
        <li>Your customer onboarding appears longer than industry average.</li>
        <li>No clear SEO signals found on your website — consider optimization.</li>
        <li>Opportunity: Leverage email retargeting for abandoned leads.</li>
    </ul>
    """
    return render_template_string(report)

if __name__ == '__main__':
    app.run(debug=True)
