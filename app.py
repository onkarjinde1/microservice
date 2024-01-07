from flask import Flask, request, render_template
import math
import socket
app = Flask(__name__)


#function to fetch host name and IP 
def fetchDetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip) 
    

def numerical_integration(lower, upper, N):
    dx = (upper - lower) / N
    result = 0.0

    for i in range(N):
        x_i = lower + i * dx
        result += abs(math.sin(x_i)) * dx

    return result

@app.route('/numericalintegralservice/<lower>/<upper>')
def integrate(lower, upper):
    lower = float(lower)
    upper = float(upper)
    integration_results = {}

    for N in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        integration_results[N] = numerical_integration(lower, upper, N)

    return integration_results


@app.route('/numericalintegralservice/<lower>/<upper>/details')
def details(lower, upper):
    hostname, ip = fetchDetails()
    
    return render_template('index.html', lower=lower, upper=upper, HOSTNAME=hostname, IP=ip)



if __name__ == '__main__':
    app.run(debug=True)