using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace UniversidadBinacionalWeb.Pages
{
	public class CarrersModel : PageModel
	{
		private readonly ILogger<CarrersModel> _logger;

		public CarrersModel(ILogger<CarrersModel> logger)
		{
			_logger = logger;
		}

		public void OnGet()
		{
		}
	}
}