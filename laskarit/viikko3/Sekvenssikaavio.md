sequenceDiagram
    participant Caller method
    participant Machine constructor
    participant FuelTank constructor
    participant FuelTank
    participant Engine constructor
    participant Engine
    participant Machine object

    Caller method ->> Machine constructor: create new Machine object
    Machine constructor ->> FuelTank constructor: create new FuelTank object
    FuelTank constructor ->> FuelTank: set fuel_contents to 0
    FuelTank constructor ->> FuelTank: fill tank with 40 units of fuel
    FuelTank constructor -->> Machine constructor: return new FuelTank object
    Machine constructor ->> Engine constructor: create new Engine object with FuelTank object as parameter
    Engine constructor ->> Engine: set _fuel_tank attribute to FuelTank object
    Machine constructor -->> Caller method: return new Machine object
    Caller method ->> Machine object: call drive method
    Machine object ->> Engine: call start method
    Engine ->> FuelTank: consume 5 units of fuel
    FuelTank -->> Engine: return updated fuel_contents
    Engine ->> Engine: check if engine is running
    Engine ->> FuelTank: consume 10 units of fuel
    FuelTank -->> Engine: return updated fuel_contents
