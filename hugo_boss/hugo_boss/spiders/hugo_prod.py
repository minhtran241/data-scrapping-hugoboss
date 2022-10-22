import scrapy


class HugoProdSpider(scrapy.Spider):
    name = "hugo_prod"
    allowed_domains = ["www.hugoboss.com"]
    start_urls = ["https://www.hugoboss.com/home"]

    def parse(self, response):
        css_categories = ".main-nav__first-level-wrapper .main-nav__first-level a.js-main-nav__first-level-link::attr(href)"
        for category_url in response.css(css_categories).getall():
            css_men_clothing = f'a[href="{category_url}"] + div a::attr(href)'
            for url in response.css(css_men_clothing).getall():
                yield scrapy.Request(url=url, callback=self.parse_clothings)

    def parse_clothings(self, response):
        css_prod = ".product-tile-plp__gallery-wrapper a::attr(href)"
        for url in response.css(css_prod).getall():
            yield response.follow(url=url, callback=self.parse_clothing)

        css_next_button = (
            ".pagingbar__items--desktop .pagingbar__item--arrow:last-child"
        )
        if response.css(css_next_button):
            yield scrapy.Request(
                url=response.css(css_next_button).css("a::attr(href)").get(),
                callback=self.parse_clothings,
            )

    def parse_clothing(self, response):
        prod_name = (
            response.css(".pdp-stage__header-title::text").get().strip()
            if response.css(".pdp-stage__header-title::text").get().strip()
            else "Unknown"
        )
        avail_colors = (
            ", ".join(response.css(".color-selector a::attr(title)").getall())
            if ", ".join(response.css(".color-selector a::attr(title)").getall())
            else "Unknown"
        )
        picUrls = (
            ", ".join(
                list(
                    map(
                        lambda pic: pic.split("?")[0] + "?wid=768&qlt=80",
                        response.css(
                            ".pdp-images__adaptive-picture img::attr(data-src)"
                        ).getall(),
                    )
                )
            )
            if ", ".join(
                list(
                    map(
                        lambda pic: pic.split("?")[0] + "?wid=768&qlt=80",
                        response.css(
                            ".pdp-images__adaptive-picture img::attr(data-src)"
                        ).getall(),
                    )
                )
            )
            else "Unknown"
        )
        detail = (
            response.css(".pdp-stage__accordion-description::text").get().strip()
            if response.css(".pdp-stage__accordion-description::text").get().strip()
            else "Unknown"
        )
        material = (
            response.css("#product-container-care-panel::text").get().strip()
            if response.css("#product-container-care-panel::text").get().strip()
            else "Unknown"
        )
        care_info = (
            ", ".join(response.css(".care-info__text::text").getall())
            if ", ".join(response.css(".care-info__text::text").getall())
            else "Unknown"
        )

        yield {
            "Product": prod_name,
            "Colors": avail_colors,
            "Pictures": picUrls,
            "Detail": detail,
            "Material": material,
            "Care Information": care_info,
        }
