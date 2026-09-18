const { handler } = require('../../api/demo-request');
exports.handler = async (event) => {
  const request = new Request(`https://${event.headers.host || 'localhost'}${event.path || '/api/demo-request'}`, {
    method: event.httpMethod,
    headers: event.headers,
    body: event.body ? (event.isBase64Encoded ? Buffer.from(event.body, 'base64').toString() : event.body) : undefined
  });
  const response = await handler(request);
  return { statusCode: response.status, headers: Object.fromEntries(response.headers), body: await response.text() };
};
