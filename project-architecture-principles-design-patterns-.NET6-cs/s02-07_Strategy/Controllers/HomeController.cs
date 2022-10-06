using Microsoft.AspNetCore.Mvc;
using Strategy.Models;
using Strategy.Services;
using System.Diagnostics;

namespace Strategy.Controllers;

public class HomeController : Controller
{
    /*
    The use of private readonly fields is beneficial for two reasons:
        • because private, it is not expose outside of the class (encapsulation).
        • because readonly, only set the value during the initialization; usually only once.
            In the case of constructor injection, this ensures that the injected dependency, referenced by
            the private field, cannot be changed by other parts of the class.
    */
    private readonly IHomeService _homeService;
    public HomeController(IHomeService homeService)
    {
        _homeService = homeService ?? throw new ArgumentNullException(nameof(homeService));
    }

    public IActionResult Index()
    {
        var data = _homeService.GetHomePageData();
        var viewModel = new HomePageViewModel(data);
        return View(viewModel);
    }

    public IActionResult Privacy()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}

