# CeneoScraper
## Etap 1 - Pobranie składowych pojedynczej opinii o wybranym produkcie z serwisu [Ceneo.pl](https://www.ceneo.pl/)
*Pobranie kodu pojedynczej strony z opiniami o wskazanym produkcie
*Analiza kodu HTML pojedynczej opinii

|Składowa opinii|Selektor CSS|Nazwa zmiennej|Typ danych|
|:--------------|:-----------|:-------------|:---------|
|Opinia|user-post|div.js_product-review|opinion||
+---------------+------------+-------------+----------+
|Identyfikator opinii|["data-entry-id"]|opionion_id||
+---------------+------------+-------------+----------+
|Autor|span.user-post__author-name|author||
+---------------+------------+-------------+----------+
|Rekomendacja|span.user-post__author-recomendation|recomm||
+---------------+------------+-------------+----------+
|Liczba gwiazdek|span.user-post_score-count|stars||
+---------------+------------+-------------+----------+
|Treść|div.user-post__text|content||
+---------------+------------+-------------+----------+
|Lista zalet|review-feature_col:has(> div.review-feature_title--positives) > review-feature_item\|pros||
||review-feature_col:has(> div[class*="positives") > review-feature_item\|||
||div.review-feature_title--positives ~ review-feature_item|||
+---------------+------------+-------------+----------+
|Lista wad|review-feature_col:has(> div.review-feature_title--negatives) > review-feature_item\|cons||
||review-feature_col:has(> div[class*="negatives") > review-feature_item\|||
||div.review-feature_title--negatives ~ review-feature_item|||
+---------------+------------+-------------+----------+
|Dla ilu osób użyteczna|span`[id^="votes-yes"]`\|useful||
||button.vote-yes > span\|||
||button.vote.yes`["data-total=vote"]`|||
+---------------+------------+-------------+----------+
|Dla ilu osób nieużyteczna|span`[id^="votes-no"]`\|useless||
||button.vote-no > span\|||
||button.vote.no`["data-total=vote"]`|||
+---------------+------------+-------------+----------+
|Czy opinia potwierdzona zakupem|div.review-pz|purchased||
+---------------+------------+-------------+----------+
|Data wystawienia opinii|span.user-post_published > time:nth-child(1)`["datetime"]`|publish_date||
+---------------+------------+-------------+----------+
|Data zakupu produktu|span.user-post_published > time:nth-child(2)`["datetime"]`|purchase_date||
+---------------+------------+-------------+----------+
