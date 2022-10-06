# a_solid_adventure_into_arch_principles_design_patterns_.NET6_C-10

This repository is based on the book An Atypical ASP.NET Code 6 Design Patterns Guide, by Carl-Hugo Marcotte.

Our objective here, is follow the chapters and the main high-level plan of the book, which is:

1. Explore basic patterns, unit testing, architectural principles, and ASP.NET Core Mechanisms.
2. Explore component scale, through patterns oriented toward small chunks of software and individual units.
3. Explore application-scale patterns and techniques, through higher-level patterns and how to structure an application as a whole.

## Section 1: Principles and Methodologies

### What is a design pattern?

From an abstract definition, design pattern is a proven technique that can be used to solve a specific problem. Take care, well-thought-out applications of design pattern should improve your application design, but throwing patterns into the mix just to use them can lead to an opposite result.

**Avoid over-engineering with as many patterns as you can. Aim to write readable code that solves the issue at hand.**

### What about a anti-patterns and code smells?

**Anti-patterns** is a proven flawed techniques that will cause some trouble and cost time and money.

Some anti-patterns can start as a viable design pattern, but through the development of the project it become a anti-pattern. For instance, **God Class**. **God Class** is a well known anti-patterns and it is a class that handles many responsibilities, other classes are in some kind of relation to it. It is the class that knows and manages everything. On the other hand, it is the class that broke the application every time someone touch it.

**The best way to solve that anti-pattern is segregate the responsibilities through multiple small classes.**

**Code smell** is a indicator of a possible problem, it does not mean that there is a problem. An example of this is a method with many comments to explain what it does. It means that the method must be split in small ones more, with proper names, more readable code.

Other examples:

1. **Control Freak**: it is related to the use of the keyword new, which means a hardcoded dependency because the creator controls the new object and its lifetime. To solve this dependency, think about dependency injection.

2. **Long methods**: it is when a method start to extend more than 10 to 15 lines of code. Some causes of a long method, can be:

1.it contains complex logic intertwined in multiple conditional statements.
2.it contains a big switch block
3.it does too many things
4.it contains duplicate code

An alternative to solver those causes can be:

1. extract one or more private methods
2. extract some code to new classes
3. reuse the code from external classes
4. a lot of conditional statements or a huge switch block, use a Chain of responsibility.

### Understand the web - request/response

### Running and building your program

|Command| Description|
|-------|------------|
|dotnet restore| Restore the dependencies (a.k.a. NuGet packages) based on the .csproj or .sln file present in the current dictionary|
|dotnet build| Build the application based on the .csproj or .sln file present in the current dictionary. It implicitly runs the restore command first|
|dotnet run| Run the current application based on the .csproj file present in the current dictionary. It implicitly runs the build and restore commands first |dotnet watch run|Watch for file changes. When a file has changed, the CLI updates the code from that file using the hot-reload feature. When that is impossible, it rebuilds the application and then reruns it (equivalent to executing the run command again). If it is a web application, the page should refresh automatically|
|dotnet test|Run the tests based on the .csproj or .sln file present in the current directory. It implicitly runs the build and restore commands first. We cover testing in the next chapter|
|dotnet watch test| Watch for file changes. When a file has changed, the CLI reruns the tests (equivalent to executing the test command again)| 
|dotnet publish|Publish the current application, based on the .csproj or .sln file present in the current directory, to a directory or remote location, such as a hosting provider. It implicitly runs the build and restore commands first|
|dotnet pack|Create a NuGet package based on the .csproj or .sln file present in the current directory. It implicitly runs the build and restore commands first. You don’t need a .nuspec file|
|dotnet clean| Clean the build(s) output of a project or solution based on the .csproj or .sln file present in the current directory|

### Automated testing

Testing is a integrated part of the development process, and in a CI/CD scenario it becomes crucial. As the application becomes bigger and more complex, tests is a good way to guarantee maintenance.

Tests can be divided in:

1. **unit tests**: are faster to run, faster to write, but are more isolated. They tend to be cheaper. Unit tests focus on individual units, like testing the outcome of a method. Unit tests **should be fast and should not rely on any infrastructure such as a database**. Unit tests should focus on testing algorithms (the ins and outs) and domain logic, not the code itself; how you wrote the code should have no impact on the intent of the test.

2. **integration tests**: Integration tests focus on the interaction between components, such as what happens when a component queries the database or what happens when two components interact with each other. Integration tests often require some infrastructure to interact with, which makes them slower to run.

3. end-to-end tests: slower to execute, lengthier to write, more integration, more expensive. End-to-end tests focus on application-wide behaviors, such as what happens when a user clicks on a specific button, navigates to a particular page, posts a form, or sends a PUT request to some web API endpoint. E2E tests focus on testing the whole application from the user’s perspective, not just part of it, as unit and integration tests do. E2E tests are usually run on actual infrastructure to test your application and your deployment

There are some testing approaches, such as: behavior-driven development (BDD), acceptance test-driven development (ATDD), test-driven development (TDD).The DevOps culture brings a
mindset to the table that focuses on embracing automated testing in line with **its continuous integration (CI) and continuous deployment (CD) ideals**. **CD is really where a robust and healthy suite of tests shine, giving you a high degree of confidence in your code, high enough to deploy the program when all tests pass.**

**TDD is a method** of developing software that states that you should write one or more tests before writing the actual code.

You invert your development flow by following the Red-GreenRefactor technique, which goes like this:
1. You write a failing test (red).
2. You write just enough code to make your test pass (green).
3. You refactor that code to improve the design by ensuring that all of the tests are still passing.

**ATDD is similar to TDD but** focuses on acceptance (or functional) tests instead of software units and involves multiple parties like customers, developers, and testers.

**BDD focuses on formulating test cases around application behaviors** using spoken language and also involves multiple parties like customers, developers, and testers. The given–when–then template defines the way to describe the behavior of a user story or acceptance test, like this:
• Given one or more preconditions (context)
• When something happens (behavior)
• Then one or more observable changes are expected (measurable side effects)

### Refactoring

Refactoring is about (continually) improving the code without changing its behavior. Having an automated test suite should help you achieve that goal and should help you discover when you break something.

### Technical debt

Technical debt represents the corners you cut short while developing a feature or a system. That
happens no matter how hard you try because life is life, and there are delays, deadlines, budgets, and people, including developers.

One way to limit the piling up of technical debt is to refactor the code often. So, factor the refactoring time into your time estimates. Another way is to improve collaboration between all the parties involved. Everyone must work toward the same goal if you want your projects to succeed.

### Testing .NET applications

**dotnet new xunit**. 

For unit testing projects, name the project the same as the project you want to test and append .Tests to it. For example, MyProject would have an associated MyProject.Tests project associated with it.

In xUnit, the [Fact] attribute is the way to create unique test cases, while the [Theory] attribute is the way to make data-driven test cases.

[Fact] attribute example:

public class FactTest
{
    [Fact]
    public void Should_be_equal()
    {
        var expectedValue = 2;
        var actualValue = 2;

        Assert.Equal(expectedValue, actualValue)
    }
}

Or:

public class AsyncFactTest
{
    [Fact]
    public async Task Should_be_equal()
    {
        var expectedValue = 2;
        var actualValue = 2;
        await Task.Yield();

        Assert.Equal(expectedValue, actualValue);
    }
}

Assertions, in xUnit, throws an exception when it fails.

Assert.Equal(expected, actual);
Assert.NotEqual(expected, actual);
Assert.Same(object_1, object_1);
Assert.NotSame(object_1, object_2);
Assert.Equal(object_1, object_2);
Assert.Null(object_1);
Assert.NotNull(object_1);

[Theory] attribute is used for more complex test cases. A theory is defined in two parts:

1. a [Theory] attribute
2. at least of the three following data attributes: [InlineData], [MemberData], [ClassData].

When writing a theory, your primary constraint is to ensure that the number of values matches the number of parameters defined in the test method. For example, a theory with one parameter must be fed with one value.

The [InlineData] attribute is the most suitable for constant values or smaller sets of values. Inline data is the most straightforward way of the three because of the proximity of the test values and the test method

public class InlineDataTest
{
    [Theory]
    [InlineData(1, 1)]
    [InlineData(2, 2)]
    [InlineData(5, 5)]
    public void Should_be_equal(int value1, int value2)
    {
        Assert.Equal(value1, value2);
    }
}

Then, the [MemberData] and [ClassData] attributes can be used to simplify the test method’s
declaration. When it is impossible to instantiate the data in the attribute, reuse the data in multiple test methods, or encapsulate the data away from the test class.
Here is an example of [MemberData] usage:

public class MemberDataTest
{
    public static IEnumerable<object[]> Data => new[]
    {
        new object[] { 1, 2, false },
        new object[] { 2, 2, true },
        new object[] { 3, 3, true },
    };
    
    public static TheoryData<int, int, bool> TypedData =>new TheoryData<int, int, bool>
    {
        { 3, 2, false },
        { 2, 3, false },
        { 5, 5, true },
    };
    
    [Theory]
    [MemberData(nameof(Data))]
    [MemberData(nameof(TypedData))]
    [MemberData(nameof(ExternalData.GetData), 10, MemberType = typeof(ExternalData))]
    [MemberData(nameof(ExternalData.TypedData), MemberType = typeof(ExternalData))]
    public void Should_be_equal(int value1, int value2, bool shouldBeEqual)
    {
        if (shouldBeEqual)
        {
        Assert.Equal(value1, value2);
        }
        else
        {
        Assert.NotEqual(value1, value2);
        }
    }

    public class ExternalData
    {
        public static IEnumerable<object[]> GetData(int start) => new[]
        {
            new object[] { start, start, true },
            new object[] { start, start + 1, false },
            new object[] { start + 1, start + 1, true },
        };
        
        public static TheoryData<int, int, bool> TypedData => new TheoryData<int, int, bool>
        {
            { 20, 30, false },
            { 40, 50, false },
            { 50, 50, true },
        };
    }
}

Last but not least, the [ClassData] attribute gets its data from a class implementing
IEnumerable<object[]> or inheriting from TheoryData<…>. The concept is the same as the other
two. Here is an example:

public class ClassDataTest
{
    [Theory]
    [ClassData(typeof(TheoryDataClass))]
    [ClassData(typeof(TheoryTypedDataClass))]
    public void Should_be_equal(int value1, int value2, bool shouldBeEqual)
    {
        if (shouldBeEqual)
        {
            Assert.Equal(value1, value2);
        }
        else
        {
            Assert.NotEqual(value1, value2);
        }
    }

    public class TheoryDataClass : IEnumerable<object[]>
    {
        public IEnumerator<object[]> GetEnumerator()
        {
            yield return new object[] { 1, 2, false };
            yield return new object[] { 2, 2, true };
            yield return new object[] { 3, 3, true };
        }
        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
    }
    
    public class TheoryTypedDataClass : TheoryData<int, int, bool>
    {
        public TheoryTypedDataClass()
        {
            Add(102, 104, false);
        }
    }
}

**It is important to note that xUnit creates an instance of the test class for every test run, so your dependencies are recreated every time if you are not using the fixtures.**

Instead, xUnit uses existing OOP concepts:
• To set up your tests, use the class constructor.
• To tear down (clean up) your tests, implement IDisposable or IAsyncDisposable and dispose
of your resources there.

#### Arrange, Act, Assert

One well-known method for writing readable tests is Arrange, Act, Assert (AAA or 3A). This technique allows you to clearly define your setup (arrange), the operation under test (act), and your assertions (assert).

[Fact]
public void Should_be_equals()
{
    // Arrange
    var a = 1;
    var b = 2;
    var expectedResult = 3;

    // Act
    var result = a + b;

    // Assert
    Assert.Equal(expectedResult, result);
}

#### Integration tests

Integration tests are harder to organize **because they depend on multiple units and can cross project boundaries and interact with various dependencies**.

#### ASP.NET Core integration testing

#### Important testing principles

**Tests test use cases (features), not the code itself.** if the expected outcome of a feature is correct, that also means the codebase is correct.

**To help with that, the test requirements usually revolve around the inputs and outputs.** The interaction between two components or two systems **should always be tied to a data contract**, whether using a classic request/response model over a REST API where the data contract is the API signature, or using an event-driven architecture approach and the data contract is the event signature or, even simpler, ComponentA returns an object that is injected into  ComponentB; the correctness of those interactions gravitates around the ins and outs.

### Architectural Principles

Fundamental architectural principles, those are the foundation of modern software engineering.

1. SOLID principles
2. The separation of concerns principle
3. DRY principle
4. KISS principle

### The SOLID principles

SOLID extends the basic OOP concepts of Abstraction, Encapsulation, Inheritance, and Polymorphism. It is also important to note that they are principles, not rules to follow at all costs. **Weigh the cost in the context of what you are building**.

The SOLID acronym represents the following:
• Single responsibility principle
• Open/Closed principle
• Liskov substitution principle
• Interface segregation principle
• Dependency inversion principle

**By following these principles, your systems should become easier to test and maintain**.

### Single responsibility principle (SRP)

the SRP means that a single class should hold one, and only one, responsibility, leading
me to the following quote: “There should never be more than one reason for a class to change.”

Software maintainability problems reduce with SRP.

Let’s review why that principle exists:
* **Applications are born to change**.
* To make our classes **more reusable and create more flexible systems**.
* To help **maintain applications**. Since you know the only thing a class does before updating it, you can quickly foresee the impact on the system, unlike with classes that hold many responsibilities, where updating one can break one or more other parts.
* To make **our classes more readable**. Fewer responsibilities lead to less code, and less code
is simpler to visualize in a few seconds, leading to a quicker understanding of that piece of
software.

SRP must not be thinking as an over-separate method because more classes in a system, the more complex to assemble the system can become, and harder it can be to debug, follow execution paths. On the other, well-separated responsibilities should lead to a better and testable system.

To follow a single responsibility, aim at packing a cohesive set of functionalities in a single class that revolves around its responsability.

To indicators of SRP violation:

1. it become harder to name a class; and remember name classes, methods and other elementos in a clear and significant way is very important.
2. a method become too big.

### What is an interface?

It is a powerful tool for creating flexible and maintainable software alike.

* The role of an interface is to define a cohesive contract (public methods, properties, and events). In its theoretical form, there is no code in an interface; it is only a contract. In practice, since C# 8, we can create default implementation in interfaces, which could be helpful to limit breaking changes in a library (such as adding a method to an interface without breaking any class implementing that interface).
* An interface should be small (ISP), and its members should align toward a common goal (cohesion) and share a single responsibility (SRP).
* In C#, a class can implement multiple interfaces, exposing multiples of those public contracts, or, more accurately, be any and all of them. By leveraging polymorphism, a class can be used as any of the interfaces it implements as well as its supertype (if any).

### Open/Closed principle (OCP)

"Software entities (classes, modules, functions, and so on) should be open for extension but closed for modification.” Bertrand Meyer.

Or in other words, you should be able to change the class behaviors from the outside without altering the code itself.

### Composition over inheritance

Composition improves code reuse since multiple classes can use those other smaller
classes. The idea is to have an object use other objects to achieve the correct behaviors instead of inheriting a base class.

Combining composition and dependency injection allows to follow the Open/Close principle.

The first appearance of the OCP, in 1988, was referring to inheritance, and OOP has evolved
a lot since then. You should, most of the time, opt for composition over inheritance.
Inheritance is still a useful concept, but you should be careful when using it; it is a concept
that is easy to misuse, creating direct coupling between classes and deep hierarchy. We
explore that more throughout the book.

### Liskov substitution principle (LSP)

The LSP focuses on preserving subtype behaviors, which leads to system stability. This principle mom linguagem de programação Java.lass, the correctness of the program does not break. 

* Any precondition implemented in a supertype should yield the same outcome in its subtypes, but subtypes can be less strict about it, never more. For example, if a supertype validates that an argument cannot be null, the subtype could remove that validation but not add stricter validation rules.

* Any postcondition implemented in a supertype should yield the same outcome in its subtypes, but aubtypes can be more strict about it, never less. For example, if the supertype never returns null, the subtype should not return null either or risk breaking the consumers of the object that are not testing for null. For example, if the supertype never returns null ,
the subtype should not return null either or risk breaking the consumers of the object that are not testing for null . On the other hand, if the supertype does not guarantee the returned value cannot be null , then a subtype could decide never to return null, making both instances interchangeable.

* Subtypes must preserve the invariance of the supertype. The behaviors of the supertype must not change. For example, a supertype must pass all the tests written for the supertype, so there is no variance between them.

* In your subtypes, add new behaviors, do not change existing ones.

### Interface Segregation Principle (ISP)

“Many client-specific interfaces are better than one general-purpose interface.”

It means:

* create interfaces
* value small interfaces more
* not try to create a multipurpose interface as 'an interface to rule them all'

**ISP is about a smaller cohesive set of functionalities that can be reused and extended**.

The last but not the least, be careful not to overuse this principle blindly. Think about cohesion and what you are trying to build, and not about how granular an interface can blindly become.

### Dependency Inversion Principle (DIP)

"One should “depend upon abstractions, [not] concretions."

Interfaces are one of the pivotal elements of our SOLID arsenal. Moreover, using interfaces is the best way to approach the DIP. Of course, abstract classes are also abstrations, but you should depend on interfaces whenever possible instead.

An abstraction class is an abstraction but is not 100% abstract, and if it is, you should replace it with an interface.

Abstract classes are used to encapsulate default behaviors that you can then inherit in sub-classes. They are helpful, but interfaces are more flexible, more powerful, and better suited to design contracts.1.
Ninja -----------> IWeapon <--------------- Sword.

### Other important principles

* Separation of concerns

    Separate your software into logical blocks, where each block is a concern. Concern can be a significant matter or a tiny detail; nonetheless, it is imperative to consider concerns when dividing your software into pieces to create cohesive units. 

* Don't repeat yourself (DRY)

    When you have duplicated logic in your system, encapsulate it and reuse that new encapsulation in multiple places instead.

* Keep it simple, stupid (KISS)

## Section 2: designing for ASP.NET core

### The Model View Controller design pattern

In a classic server-rendered web user interface, the objective of the MVC pattern is to separate the rendering of a page into three distinct components that interact each other. It helps have smaller pieces that are easier to maintain instead of one bigger piece.

Then, MVC divide application into three distinct parts, where each has a single responsibility:

* model: it is a data structure representing the domain that we are modeling
* view: it is to present a model to a user as a web user interface, so mainly HTML, CSS, JS
* controller: it is the key component. It plays a coordinating role between the request from a user and its response. The controller's code should remain minimal and should not include complex logic or manipulation. The controller's primary responsibility is to handle requests and dispatch responses. The controller is an HTTP bridge.

### Anatomy of ASP.NET Core MVC

**Controller**: through a easiest way a controller may be created as a class inheriting from Microsoft.AspNetCore.Mvc.Controller.

* A controller exposes one or more actions
* an action can take zero or more input parameters
* an action can return zero or one output value
* the action is what handles the actual request
* we can group cohesive actions under the same controller, thus creating a unit.

**Model**: it is a class that contain properties and methods.

**View**: Razor is a C#-based templating language that allows creating HTML-like pages and views (there is also a VB.NET version). Razor is a very convenient way of writing complex web UI logic productively. Razor views are stored in .cshtml files. The Razor view engine compiles that markup to C# classes
that ASP.NET Core MVC leverages to render the HTML to the users.

### Default routing

ASP.NET Core has a routing mechanism that allows developers to define one or more routes to know **which controller should handle a specific HTTP request**. **A route is a URL template that maps HTTP requests to C# code**.

Let's take a look at MVC template Program.cs files.

`app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");`

* controller:
    * {controller} maps the request to a {controller}Controller class. For example, Home would map to the HomeController class.
    * {controller=Home} means that the HomeController class is the default controller, which is used if no {controller} is supplied.
* actions:
    * {action} maps the request to a controller method.
    * {action=Index} means that the Index method is the default action. For example. if we had a ProductsController class in our application, making a GET request to https://localhost/Products would make MVC invoke the ProductsController.Index() method. Note that in a CRUD controller (create, read, update, delete), Index is where you usually define your list.
* parameter
    * {id} means that any value following the action name maps to the id parameter of that action method.
    * the ? in {id?} means the parameter is optional
    * some examples:
        * /Some/Action would map to SomeController.Action()
        * /Some would map to SomeController.Index()
        * / would map to HomeController.Index()
        * /SomeAction/123 would map to SomeController.Action(123)

MVC and Solid. Using MVC it is possible explore some aspects of SOLID, not all.

* S = the MVC pattern divides the rendering of a page into three different roles
* O = N/A
* L = N/A
* I = based on the three small responsibilities that were created from the three roles of MVC, up to a certain extent we have to dealing with three interfaces. However, controllers can become bloated with capabilities and contain many actions. a simple CRUD controller has a total of eight actions to begin with: one action for the list and the details page, and two actions for the create, edit, and delete pages. From there if you add more capabilities, the controller will just become fatter and fatter. One way to help is to create reusable components.
* D = N/A

### View Model design pattern

**The view model comes into play where the application access data from a data source and then render a view based on that data. But instead of sending the raw data to the view, the required data is copied to another class that carries only the required data to render**.

It is allowed presentation-centric features to the view model, composing with filtering, sorting without altering data domain models. And so, in line with Single Responsibility Principles (ISP) 

The main goal of a View Model is decoupling the other parts of the software from the view, creating a model specific to a view.

Some benefits are: views are not coupled with each other, reducing the maintenance issues; view models allow developers to gather data in a particular format and send it to the view in another one that's better suited for rendering that specific view, improving the application's testability, quality and stability.

**The View Model defines a clear line between the user interfaces and the domain, decoupling model from the view.**

Using the View Model pattern helps us follow the SOLID principles in the following ways:
* S: A view model **adds clear boundaries between the domain model and the view**, leading to **two distinct responsibilities to help keep things isolated**.
* O: N/A
* L: N/A
* I: A view model allows us to **limit the amount of information sent to the view**, keeping that information to a minimum. The **View Model pattern introduces two possibly smaller interfaces: one for the view and one for the domain**.
* D: N/A

In summary, view model helps to decouple the model from the presentation. Then, the view has only one responsibility, which is display the UI.

## Section 3: MVC pattern for Web APIs

### An overview of REST

REST is a way to create internet-based services, that commonly use HTTP. It allows the well-known HTTP specifications to be reused instead of recreating new ways of exchanging data.

* each HTTP endpoint is a resource
* each resource can be secured independently
* calling the same resource twice should result in the same operation executed twice. Executing two POST /entities result in two new entities; GET /entities/some-id return the same entity twice.
* the service should be stateless, which means that it does not persist information about its clients between requests.
* the response from a RESTful service (GET) should be cacheable

### HTTP methods

HTTP methods are also known as verbs:

GET: read data: a list or a single entity; success status code is 200 ok;
POST: create a new entity; success status code is 201 created;
PUT: replace an entity; success status code is 200 ok or 204 no content;
DELETE: delete an entity; success status code is 200 ok or 204 no content;
PATCH: partially update an entity; success status code is 200 ok.

### Status code

|Status code| role|
|-----------|-----|
|200 OK |Tells the client the request has succeeded. **It usually includes data related to an operation or an entity in the body of the response**|
|201 CREATED|Tells the client the request has succeeded and the system created a resource. **It should also include a Location HTTP header pointing to the newly created resource and including the new entity in the response body**|
|202 ACCEPTED|Tells the client **the request has been accepted for processing but is not processed yet**. In an event-driven system (see Chapter 16, Introduction to Microservices Architecture), this could mean that an event has been published, the current resource has completed its job (published the event), but to know more, the client needs to contact another resource, wait for a notification, just wait, or can’t know|
|204 NO CONTENT|Tells the client the request has succeeded with no content in the response body|
|302 FOUND|Tells the client to follow the specified Location header, which represents the redirection target|
|400 BAD REQUEST|Tells the client about a validation error, generally related to badly formatted input data, missing data, or something similar|
|401 UNAUTHORIZED|Tells the client that it must authenticate to access the resource|
|403 FORBIDDEN|Tells the client that it does not have the required rights to access the resource (authorization)|
|404 NOT FOUND|Tells the client that the resource does not exist or was not found|
|409 CONFLICT|Tells the client that a conflict has occurred. A typical scenario would be that the entity has changed between its last GET and its current operation (likely a PUT request)|
|500 INTERNAL SERVER ERROR|Tells the client that an unhandled error occurred on the server side and prevented it from fulfilling the request|

* The 1XX status code (omitted from the preceding table) represents informational continuation results, usually handled automatically by the server, such as 100 Continue and 101 Switching Protocols.
* 2XX are successful results.
* 3XX are related to redirections.
* 4XX are request errors (from the client side), usually introduced by the user, such as an empty required field.
* 5XX are server-side errors that the client cannot do anything about.

### HTTP headers

Web services leverage HTTP headers to transmit client's information and describe their options and capabilities.

* Location hearder: after creating an entity (201 created), the Location header should point to the GET endpoint where the client can access that new entity; After starting an asynchronous operation (202 Accepted), the Location header could point to the status endpoint where you can poll for the state of the operation (has it completed, failed, or is it still ongoing); when redirecting a client, the Location header contains the destination URL.
* Retry-after: it can also come in handy when mixed with 202 Accepted, 301 Moved Permanently, 429 Too many Requests, or 503 Service Unavailable.
* ETag: it identify the version of the entity and can be used in conjunction with If-Match to avoid mid-air-collision. The ETag and If-Match headers form a sort of optimistic concurrency method that prevents request two from overwriting changes made by request one when changes are happening simultaneously or not in the expected order; a.k.a. a way to manage conflicts.

### Versioning

It is a crucial aspect of REST API. It helps the API clients to query specific API versions when the contract changes **because both ends of the pipe must know what to expect, what API contract to respect.**

### Default versioning strategy

The best way as a default versioning is return the first version. It preserves backward compatibility and it does not break the consumers if more endpoints are added.

### Versioning strategy

A simple way to solve that could be leverage URL patterns to define and include the API version, such as https: //localhost/v2/some-entities. This is easier to query from a browser, making it simple to know the version ar a glance, but the endpoint is not pointing to a unique resource anymore (**a key principle of REST**) as each resource has one endpoint for each version.

Another way is to use HTTP header, including a custom header like api-version or Accept-version or the Accept standard header. Through that the resources have unique endpoints while enabling multiple version of each entity.

### Wrapping up

With a method (verb), the client can express the intent to create, update, read, or delete an entity;
With a status code, the endpoint can tell the client the state of the operations;
By adding more headers, client and endpoint can add more metadata to the request or response;
By adding versioning, the endpoint can evolve without breaking existing clients while giving options to consumers about the version they want to consume.

## Section 4: Model View Controller design pattern

Good reasons to implement web APIs

* it is an efficient way of sharing data between systems
* it allows interoperability between technologies by dialoguing in universal languages, such as JSON or XML
* it allows your backend to be centralized and shared with multiple frontends such as mobile, desktop, and web application;
* it allows you to gate (secure, protect, or hide) downstream systems, with APIs acting as gateways;
* it allows the encapsulation of units of logic in reusable, independent, and possibly even tiny systems.

### Goal

From the web API perspective, MVC pattern has the following task: **separate displaying (serializing) and entity into three distinct components that interact with each other** because doing that it helps have smaller pieces that are easier to maintain and test than big bloated ones that are very hard to test in isolation.

### Design

Three single responsibilities:

* model: it is a data structure representing the domain that we are modeling;
* view: it is to present a model to a user
* controller: it is the key component of MVC. It plays the coordinator role between a request from a user to its response. The code of a controller should remain minimal and should not include complex logic or manipulation. The controller's primary responsibility is to handle a request and dispatch a response. **It is an HTTP bridge**

## Section 5: Anatomy of ASP.NET Core Web APIs

To generate a new web api use the command dotnet new webapi

### The entry point

The first piece is the entry point: Program.cs. In this files there are:

* registration: `builder.Services.AddControllers();`, `app.MapControllers();`
* the default template also registers Swagger to generate OpenAPI specs automatically and a UI to visualize them.

### Controller

The easiest way to create a controller is create a class that inherits from ControllerBase. Another way is just decorate a class with [ApiController] attribute. By convention, the controller's class name is suffixed by Controller.

ControllerBase, ApiControllerAttribute and attribute routing classes come form Microsoft.AspNetCore.Mvc namespace

### Returning values

The objectives of building a web API is to return data to its consumers and execute remote operations securely.

Most of the plumbing is done by the ASP.NET core code, let's take a look at some helpers provided by the ControllerBase class:

* **StatusCode method** allows specifying the status code to return. One can use constants defined in the StatusCode class to help or pass an int directly. See: https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes?view=aspnetcore-6.0

* The Ok method allows returning a status code 200 ok with an optional body

* The created, CreatedAction, and other similar methods allow returning a status code 201 Created, including different options to **craft the Location URL representing the newly created resource**and optionally serialize that new entity as part of the response body.

* The NoContent method allows returning a status code 204 No Content and an empty body

* The NotFound method allows returning a status code 404 Not Found with an optional body

* The BadRequest method allows returning a status code 400 Bad Request with an optional body representing the problems.

* The Redirect, RedirectPermanent, and other similar methods allow returning a redirection status code like 302 Found and 301 Moved Permanently while exposing different options to craft the Location URL representing the redirection the client should follow.

* The Accepted, AcceptedAtAction, and other similar methods allow the status code 202 Accepted to be returned, along with an optional body and different options to craft the Localtion URL representing the status endpoint.

* The Conflict method allows the status code 409 Conflict to be returned with an optional body representing the error.

There are at least four ways to return data to the client of API:

* return the model directly
* return an ActionResult<TValue> class
* return an ActionResult class
* return an IActionResult interface

* IActionResult interface and ActionResult class are more abstract, constraining to use the helper methods exposed by ControllerBase or construct the resulting instances to return values. And they are not auto-discoverable by OpenAPI tools like Swagger.

To solve the API discoverability, it could decorate the actions with the ProducesResponseType attribute:

`[ProducesResponseType(typeof(WeatherForecast[]), StatusCodes.Status200OK)]`

public IEnumerable<WeatherForecast> Get() => GetWeatherForecasts();

public ActionResult<IEnumerable<WeatherForecast>> GenericClassActionDirect() => GetWeatherForecasts();

public ActionResult<IEnumerable<WeatherForecast>> GenericClassActionOk() => Ok(GetWeatherForcasts());

public ActionResult<IEnumerable<WeatherForecast>> GenericClassActionNotFound() => NotFound();

### Attribute routing

**Attribute routing maps an HTTP request to a controller action**, and the attributes decorate the controllers and the actions to create the complete routes.

[ApiController]
[Route("[controller]")]

public class ValuesController : ControllerBase
{
    [HttpGet]
    public ActionResult<IEnumerable<string>> Get() => default!;
    [HttpGet("{id}")]
    public ActionResult<string> Get(int id) => default!;
    [HttpPost]
    public void Post([FromBody] string value) { }
    [HttpPut("{id}")]
    public void Put(int id, [FromBody] string value) { }
    [HttpDelete("{id}")]
    public void Delete(int id) { }
}

[Route("[controller]")] means that the actions of this controller are reachable through /values. Then the other attributes tell ASP.NET **to map** specific requests to specific methods. 
For example: 
[HttpGet] tells ASP.NET that GET /values should be map to the Get() method
[HttpGet("{id}")] tells APS.NET that GET /values/1 requests should be routed to the Get(int id) method.

**When designing a web API, the URL leading to yourl-studiong the consumers of a web API endpoint**.

The goal is to control the inputs and outputs of an endpoint **by decoupling the API contract from the application's inner working**, defining an API without thinking about the underlying data structures. The goal is design endpoints that are easier to consume, maintain and evolve.

A data transfer object allows to design an API endpoint with a specific data contract (input and output) **instead of exposing the domain model**. **This separation between the presentation and the domain is a crucial** element that leads to having multiple independent components instead of a bigger, more fragile one.

### API Contracts

An API contract is the definition of a web API, because a consumer should know how to call an endpoint and what to expect from it in return. Each endpoint should have a signature and should enforce that signature.

A contract, from dev perspective, is a model associated with a URI and an HTTP method.

## Section 6: Understanding the Strategy, abstract factory, and singleton design patterns

### strategy design pattern

**It is a behavioral design pattern that allows us to change object behaviors at runtime**. **It alows us to compose complex object tree and rely on it to follow the Open/Closed Principle (OCP)**. Strategy pattern plays a significant role in the composition over inheritance way of thinking.

The goal of strategy pattern is to extract an algorithm (strategy) from the host class needing it, allowing the consumer to decide on the strategy to use at runtime. 

For example: we could design a system that fetches data from two different types of databases. Then we could apply the same logic over that data and use the same over interface to display it. Using the strategy pattern, we could crate two strategies, FetchDataFromSQL and FetchDataFromCosmosDb, both contracted with IStrategy. So, we could plug the strategy that we need at runtime in the context class. That way, when the consumer calls the context, the context does not need to know where the data comes from, how it is fetched, or what strategy is in use; it only gets what it needs to work, delegating the fetching responsibility to an abstracted strategy.

FetchDataFromSQL:IStrategy
+ ExecuteAlgo():void

FetchDataFromCosmosDb:IStrategy
+ ExecuteAlgo():void

ContextClass
-IStrategy fetch_database
+SomeOperation():void

The building blocks of the **Strategy pattern** go as follows:
* Context is a class that **delegates one or more operations to an IStrategy implementation**.
* **IStrategy is an interface defining the strategies**.
* FetchDataFromSQL and FetchDataFromCosmosDb represent one or more different concrete implementations of the IStrategy interface.

That is the strength of the Strategy pattern: it abstracts the implementation away from both the Context and the consumer. Because of that, we can change the strategy during either the object creation or at runtime without the object knowing, changing its behavior on the fly.

The Strategy design pattern is very effective at delegating responsibilities to other objects, allowing you to delegate the responsibility of an algorithm to other objects while keeping its usage trivial. It also allows having a rich interface (context) with behaviors that can change during the program’s execution.

Meanwhile, the Strategy pattern is excellent at helping us follow the SOLID principles:

* S: It helps to extract responsibilities to external classes and use them, interchangeably, later.
* O: It allows extending classes without updating its code by changing the current strategy at
runtime.
* L: It does not rely on inheritance. Moreover, it plays a large role in the composition over inheritance principle, helping us avoid inheritance altogether and, at the same time, the LSP.
* I: By creating smaller strategies based on lean and focused interfaces, the Strategy pattern is an excellent enabler for respecting the ISP.
D: The creation of dependencies is moved from the class using the strategy (the context) to the
class’s consumer. That makes the context depend on abstraction instead of implementation,
inverting the flow of control.

### abstract factory design pattern

It is a creational design pattern, used to create other objects. The Strategy pattern is the backbone of dependency injection, enabling the composition of complex object trees, while factories are used to create some of those complex objects that can’t be assembled automatically by a dependency injection library.

**The abstract factory pattern goal is to abstract the creation of a family of objects**. 

With Abstract Factory, the consumer asks for an abstract object and gets one. The factory is an
abstraction, and the resulting objects are also abstractions, decoupling the object creation from the consumers.

For example:

* IVehicleFactory is an Abstract Factory defining two methods: one that creates cars of type
ICar and another that creates bikes of type IBike.
* HighGradeVehicleFactory is an implementation of the Abstract Factory that handles highgrade vehicle model creation. This concrete factory returns instances of type HighGradeCar
or HighGradeBike.
* LowGradeVehicleFactory is an implementation of our Abstract Factory that handles lowgrade vehicle model creation. This concrete factory returns instances of type LowGradeCar
or LowGradeBike.
* LowGradeCar and HighGradeCar are two implementations of ICar.
* LowGradeBike and HighGradeBike are two implementations of IBike.

**A consumer uses the IVehicleFactory interface and should not be aware of the concrete factory used underneath, abstracting away the vehicle creation process**.

Abstract Factory is an excellent pattern to abstract away the creation of object families, isolating each family and its concrete implementation, leaving the consumers unaware of (decoupled from) the family being created at runtime.

Abstract Factory pattern can help us follow the SOLID principles:

* S: Each concrete factory has the sole responsibility of creating a family of objects. You could combine Abstract Factory with other creational patterns such as the Prototype and Builder
patterns for more complex creational needs.
* O: The consumer is open to extension but closed for modification; as we did in the “expansion”
sample, we can add new families without modifying the code that uses it.
* L: We are aiming at composition, so there’s no need for any inheritance, implicitly discarding
the need for the LSP. If you use abstract classes in your design, you need to make sure you
don’t break the LSP when creating new abstract factories.
* I: By extracting an abstraction that creates other objects, it makes that interface very focused
on one task, which is in line with the ISP, creating flexibility at a minimal cost.
* D: By depending only on interfaces, the consumer is not aware of the concrete types that it
is using.

### Singleton design pattern

It allows creating and reusing a single instance of a class. We are exploring the Singleton pattern in this chapter because it relates to dependency injection.

The singleton pattern goal is to limit the number of instances of a class to one. A singleton encapsulates both the object logic itself and its creational logic.

**The Singleton pattern promotes that one object must have two responsibilities, breaking the Single Responsibility Principle (SRP). A singleton is the object and its own factory**.

**Singleton class is composed of the following**:

* A private static field that holds its unique instance.
* A public static Create() method that creates or returns the unique instance.
* A private constructor, so external code cannot instantiate it without passing by the Create
method.
* Singleton pattern allows creation of a single instance class for the whole lifetime of the program.
* Considering SOLID principles:
    * S: Singleton pattern violates that principles because it has two responsibilities: a. creation responsibility, b. creating and managing itself (lifetime management).
    * O: Singleton pattern violates that principle because it limits extensibility, the class must be modified to be updated, impossible to extend without changing the code.
    * L: Singleton does not violates that principle because there isn't inheritance directly involved.
    * I: There is no interface involved, so it is violated.
    * D: The singleton class has a rock-solid hold on itself. It also suggests using its static property (or method) directly without using an abstraction, breaking the DIP with a sledgehammer.

## Section 7: Deep Dive into Dependency Injection

### What is dependency injection?

DI is a way to apply Inversion of Control principle, which means, in a broader sense, the D from SOLID, that is, dependency inversion principle.

The basic idea is move the creation of dependencies from the objects themselves to the program's entry point. For that the interfaces are used.

For example: an object should not know about a specific object B that it is using. Rather, A should use, and consequently know, an interface I, which is implemented by B, and B should be resolved and inject at runtime.

Let’s decompose this:
* Object A should depend on interface I instead of concretion B .
* Instance B , injected into A , should be resolved at runtime by the IoC container.
* A should not be aware of the existence of B .
* A should not control the lifetime of B.

### Object Lifetime

* Transient: The container creates a new object every time you ask for one; For instance: services.AddTransient<ISomeService, SomeService>()
* Scoped: The container creates an object per HTTP request and passes that object around to all other objects that want to use it. For instance, services.AddScoped<ISomeService, SomeService>()
Singleton: The container creates a single instance of that dependency and always passes that unique object araound. For instance, services.AddSingleton<ISomeService, SomeService>()

### New keyword and Freak Control Smell Code

What is the problem with the new keywork? In the context of dependency injection, the new keyword brings a question: the creation of the object should be done here? Or, to manage the dependency, is it necessary a container to handle it and the dependency must be injected?

There're two scenarios:

* stable dependencies, as the name suggest, are dependencies that not break the application when a new version is released, for they use a deterministic code, a.k.a. Liskov Substituition Principle (LSP). Speaking from the perspective of .NET, data structures, data transfer objects (DTO), List<T>, elements that are part of the .NET could be considered stable dependencies. 
* volatile dependencies are dependencies that **can change**, **behaviors that could be swapped**, or elements you may want to extend, basically, **most of the classes you create for your programs such as data access and business logic classes**. These are the dependencies that you should no longer instantiate using the new keyword. The primary way to break the tight coupling between implementations is **to rely on interfaces instead**.

**When in doubt, inject the dependency instead of using the new keyword**

### Strategy Pattern

Strategy pattern is a way to compose complex object trees using dependency injection to dynamically create those instances.

Strategy pattern is a behavioral pattern through which is possible compose object trees at runtime, giving flexibility and control over objects' behavior. That pattern call the Composition over Inheritance principle.

There're three common ways to inject dependency into objects:

* constructor injection: injecting dependencies into the constructor as parameters, and is useful for injecting required dependencies.
* property injection: is useful to inject optional dependencies into properties.
* method injection: is also used to inject optional dependencies into classes 

