# Actor Simulator

# Description
The Actor Simulator is a Python-based simulation tool that mimics the behavior of actuators by changing and storing their states (on/off). It utilizes the MQTT protocol for communication and can be managed through MQTT Explorer.

# Requirements
To run the Actor Simulator, you'll need the following software and dependencies:

Python 3.x
Docker
MQTT Explorer
Paho MQTT library

# Installation
To set up the Actor Simulator, follow these steps:

## Clone the repository:
```
git clone https://github.com/Githumaru/actor-simulator.git
cd actor-simulator
```

## Create and start the Docker containers using Docker Compose:
```
docker-compose up -d
```

# Usage
Connect to the MQTT broker at port 1883 using MQTT Explorer.

Two actors are available: "Valve" and "Switch."

Changing Actor State

To change the state of an actor, send a message to the "request" topic with the following format:

```
<ActorName> set <State>
```

```
<ActorName>: The name of the actor (e.g., "Valve" or "Switch").
```

```
set: The command to set the state.
```

```
<State>: The desired state, either "On" or "Off."
```

Example:
Valve set On

Querying Actor State

To query the state of an actor, send a message to the "request" topic with the following format:

```
<ActorName> get
```

```
<ActorName>: The name of the actor (e.g., "Valve" or "Switch").
```

```
get: The command to get the state.
```

Example:
Switch get
