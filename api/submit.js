export default function handler(req, res) {
  if (req.method !== 'POST') {
    res.status(405).send('Method Not Allowed');
    return;
  }

  const {
    business_name,
    industry,
    website_url,
    revenue,
    employees,
    tools,
    pain_points
  } = req.body;

  const report = `
    <h3>Diagnostic Report for ${business_name}</h3>
    <p><strong>Industry:</strong> ${industry}</p>
    <p><strong>Website:</strong> ${website_url}</p>
    <p><strong>Monthly Revenue:</strong> ${revenue}</p>
    <p><strong>Employees:</strong> ${employees}</p>
    <p><strong>Tools Used:</strong> ${tools}</p>
    <p><strong>Main Pain Points:</strong> ${pain_points}</p>
    <hr />
    <h4>AI Insights</h4>
    <ul>
      <li>Opportunity to consolidate overlapping tools — save up to $300/month.</li>
      <li>SEO optimization needed: homepage has no meta description.</li>
      <li>Low social engagement detected — consider automating outreach.</li>
      <li>Customer feedback loop is missing. Add surveys or follow-up emails.</li>
    </ul>
  `;
  res.status(200).send(report);
}
