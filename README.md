**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

PODS

![Pods](/answer-img/pods.PNG)

SERVICES

![Services](/answer-img/services.PNG)


## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

![Home page](/answer-img/homepage.PNG)

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

![Source](/answer-img/source.PNG)

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

-Service Level Indicator (SLI) is a measurement we use for the goal e.g uptime and traffic of an application
-Service Level Objective (SLO) is a goal that we wants to reach e.g have an uptime of 99.9% during the month or 99.5% req/secs in a week

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs.
 
-Uptime - The percentage of time a microservice is up and working as expected. Pod uptime >= 99.5%99.999 %
-Resource Saturation - The usage of resources by a particular microservice. (CPU and Memory Utilization)
-Traffic - Request/second
-Latency - Time taken by a microservice to respond to a request. Usually measured as average
-Errors - The percentage of requests to a service/component that fail such as 4xx or 5xx errors.


## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

![Uptime-Error](/answer-img/uptime-error.PNG)


## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

![Jaeger-UI](/answer-img/jaegerUI.png)

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

![Jaeger-metric](/answer-img/jaeger.png)


## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name:  HTTP 500 error status - Backend-app 

Date: 12:11:2021 20:00pm

Subject: MongoDB service not accessible

Affected Area: Backend service

Severity: HIGH

Description: The MongoDB resource in backend service is not accessible for it to process POST requests from backend service.


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

-Application uptime should be >= 99.999 % in period of one month
-Successfull per service request should be >= 99.99% requests
-All Services with successful responses should be  >= 99.99% requests

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

1. Uptime
  -Pod Uptime
  -Success Requests Percentage/second
  -Service Success 
2. Error Rate
  -Number of Errors/second
  -Error Response Rate/second
3. Traffic
  -Number of Requests/second
  -Number of Successful Requests/0.5s
4. Latency
  -Response Time average
  -Resource Usage/Saturation
5. Memory Usage 
  -CPU Utilization 
  -Memory Utilization 

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

![Final-Dashboard](/answer-img/finaldashboard.png)
