===============================
blockdiagcontrib-nationalflags
===============================
A plugin for `blockdiag` that provides shapes for national-flags.
The shapes are using `National Flags`_ images provided by `Wikipedia`_ .

.. _National Flags: http://ja.wikipedia.org/wiki/%E5%9B%BD%E6%97%97%E3%81%AE%E4%B8%80%E8%A6%A7
.. _Wikipedia: http://www.wikipedia.org/

Diagram examples
================
`blockdiagcontrib-nationalflags` renders network icon as node's shape.

Example::

   diagram admin {
     A [shape = "nationalflag.japan"];
   }

.. blockdiag::

   diagram admin {
     A [shape = "nationalflag.japan"];
   }

Or, use `shape_namespace` keyword::

   diagram admin {
     shape_namespace = "nationalflag";

     A [shape = "japan"];
   }

.. blockdiag::

   diagram admin {
     shape_namespace = "nationalflag";

     A [shape = "japan"];
   }

See more examples and output images in http://packages.python.org/blockdiagcontrib-nationalflags/ .


Requirements
============
* blockdiag 0.9.1 or later


License
=======
Python Software Foundation License.


Shapes
=======

.. list-table::
   :header-rows: 0

   * - shape = "nationalflag.greece"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.greece"]; }

     - shape = "nationalflag.lebanon"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.lebanon"]; }

   * - shape = "nationalflag.estonia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.estonia"]; }

     - shape = "nationalflag.panama"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.panama"]; }

   * - shape = "nationalflag.morocco"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.morocco"]; }

     - shape = "nationalflag.burkina_faso"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.burkina_faso"]; }

   * - shape = "nationalflag.belize"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.belize"]; }

     - shape = "nationalflag.nicaragua"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.nicaragua"]; }

   * - shape = "nationalflag.iran"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.iran"]; }

     - shape = "nationalflag.hungary"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.hungary"]; }

   * - shape = "nationalflag.palestine"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.palestine"]; }

     - shape = "nationalflag.saint_vincent_and_the_grenadines"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.saint_vincent_and_the_grenadines"]; }

   * - shape = "nationalflag.guatemala"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.guatemala"]; }

     - shape = "nationalflag.maldives"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.maldives"]; }

   * - shape = "nationalflag.mexico"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.mexico"]; }

     - shape = "nationalflag.senegal"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.senegal"]; }

   * - shape = "nationalflag.armenia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.armenia"]; }

     - shape = "nationalflag.samoa"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.samoa"]; }

   * - shape = "nationalflag.japan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.japan"]; }

     - shape = "nationalflag.transnistria"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.transnistria"]; }

   * - shape = "nationalflag.lesotho"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.lesotho"]; }

     - shape = "nationalflag.the_democratic_republic_of_the_congo"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_democratic_republic_of_the_congo"]; }

   * - shape = "nationalflag.guinea_bissau"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.guinea_bissau"]; }

     - shape = "nationalflag.honduras"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.honduras"]; }

   * - shape = "nationalflag.rwanda"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.rwanda"]; }

     - shape = "nationalflag.latvia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.latvia"]; }

   * - shape = "nationalflag.georgia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.georgia"]; }

     - shape = "nationalflag.switzerland"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.switzerland"]; }

   * - shape = "nationalflag.somalia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.somalia"]; }

     - shape = "nationalflag.grenada"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.grenada"]; }

   * - shape = "nationalflag.belarus"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.belarus"]; }

     - shape = "nationalflag.east_timor"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.east_timor"]; }

   * - shape = "nationalflag.peru"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.peru"]; }

     - shape = "nationalflag.monaco"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.monaco"]; }

   * - shape = "nationalflag.iraq"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.iraq"]; }

     - shape = "nationalflag.venezuela_(state)"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.venezuela_(state)"]; }

   * - shape = "nationalflag.kazakhstan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.kazakhstan"]; }

     - shape = "nationalflag.slovenia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.slovenia"]; }

   * - shape = "nationalflag.belgium"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.belgium"]; }

     - shape = "nationalflag.spain"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.spain"]; }

   * - shape = "nationalflag.the_united_states"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_united_states"]; }

     - shape = "nationalflag.finland"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.finland"]; }

   * - shape = "nationalflag.australia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.australia"]; }

     - shape = "nationalflag.trinidad_and_tobago"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.trinidad_and_tobago"]; }

   * - shape = "nationalflag.myanmar"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.myanmar"]; }

     - shape = "nationalflag.paraguay"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.paraguay"]; }

   * - shape = "nationalflag.barbados"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.barbados"]; }

     - shape = "nationalflag.kosovo"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.kosovo"]; }

   * - shape = "nationalflag.cuba"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.cuba"]; }

     - shape = "nationalflag.qatar"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.qatar"]; }

   * - shape = "nationalflag.pakistan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.pakistan"]; }

     - shape = "nationalflag.south_ossetia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.south_ossetia"]; }

   * - shape = "nationalflag.angola"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.angola"]; }

     - shape = "nationalflag.russia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.russia"]; }

   * - shape = "nationalflag.sweden"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.sweden"]; }

     - shape = "nationalflag.kuwait"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.kuwait"]; }

   * - shape = "nationalflag.nagorno_karabakh"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.nagorno_karabakh"]; }

     - shape = "nationalflag.jamaica"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.jamaica"]; }

   * - shape = "nationalflag.uzbekistan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.uzbekistan"]; }

     - shape = "nationalflag.canada"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.canada"]; }

   * - shape = "nationalflag.chile"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.chile"]; }

     - shape = "nationalflag.liberia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.liberia"]; }

   * - shape = "nationalflag.the_republic_of_china"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_republic_of_china"]; }

     - shape = "nationalflag.india"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.india"]; }

   * - shape = "nationalflag.the_sahrawi_arab_democratic_republic"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_sahrawi_arab_democratic_republic"]; }

     - shape = "nationalflag.tanzania"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.tanzania"]; }

   * - shape = "nationalflag.ukraine"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.ukraine"]; }

     - shape = "nationalflag.botswana"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.botswana"]; }

   * - shape = "nationalflag.swaziland"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.swaziland"]; }

     - shape = "nationalflag.gabon"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.gabon"]; }

   * - shape = "nationalflag.bangladesh"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.bangladesh"]; }

     - shape = "nationalflag.argentina"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.argentina"]; }

   * - shape = "nationalflag.the_gambia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_gambia"]; }

     - shape = "nationalflag.the_united_arab_emirates"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_united_arab_emirates"]; }

   * - shape = "nationalflag.uruguay"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.uruguay"]; }

     - shape = "nationalflag.the_czech_republic"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_czech_republic"]; }

   * - shape = "nationalflag.bulgaria"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.bulgaria"]; }

     - shape = "nationalflag.fiji"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.fiji"]; }

   * - shape = "nationalflag.nauru"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.nauru"]; }

     - shape = "nationalflag.egypt"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.egypt"]; }

   * - shape = "nationalflag.the_bahamas"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_bahamas"]; }

     - shape = "nationalflag.thailand"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.thailand"]; }

   * - shape = "nationalflag.azerbaijan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.azerbaijan"]; }

     - shape = "nationalflag.indonesia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.indonesia"]; }

   * - shape = "nationalflag.sierra_leone"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.sierra_leone"]; }

     - shape = "nationalflag.sao_tome_and_principe"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.sao_tome_and_principe"]; }

   * - shape = "nationalflag.chad"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.chad"]; }

     - shape = "nationalflag.sri_lanka"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.sri_lanka"]; }

   * - shape = "nationalflag.cyprus"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.cyprus"]; }

     - shape = "nationalflag.ireland"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.ireland"]; }

   * - shape = "nationalflag.liechtenstein"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.liechtenstein"]; }

     - shape = "nationalflag.italy"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.italy"]; }

   * - shape = "nationalflag.mongolia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.mongolia"]; }

     - shape = "nationalflag.the_comoros"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_comoros"]; }

   * - shape = "nationalflag.turkey"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.turkey"]; }

     - shape = "nationalflag.vietnam"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.vietnam"]; }

   * - shape = "nationalflag.tajikistan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.tajikistan"]; }

     - shape = "nationalflag.poland"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.poland"]; }

   * - shape = "nationalflag.tuvalu"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.tuvalu"]; }

     - shape = "nationalflag.the_netherlands"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_netherlands"]; }

   * - shape = "nationalflag.ecuador"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.ecuador"]; }

     - shape = "nationalflag.lithuania"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.lithuania"]; }

   * - shape = "nationalflag.syria"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.syria"]; }

     - shape = "nationalflag.the_republic_of_the_congo"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_republic_of_the_congo"]; }

   * - shape = "nationalflag.jordan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.jordan"]; }

     - shape = "nationalflag.eritrea"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.eritrea"]; }

   * - shape = "nationalflag.the_cook_islands"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_cook_islands"]; }

     - shape = "nationalflag.austria"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.austria"]; }

   * - shape = "nationalflag.guyana"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.guyana"]; }

     - shape = "nationalflag.moldova"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.moldova"]; }

   * - shape = "nationalflag.vanuatu"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.vanuatu"]; }

     - shape = "nationalflag.bosnia_and_herzegovina"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.bosnia_and_herzegovina"]; }

   * - shape = "nationalflag.el_salvador"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.el_salvador"]; }

     - shape = "nationalflag.albania"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.albania"]; }

   * - shape = "nationalflag.madagascar"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.madagascar"]; }

     - shape = "nationalflag.kiribati"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.kiribati"]; }

   * - shape = "nationalflag.dominica"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.dominica"]; }

     - shape = "nationalflag.zambia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.zambia"]; }

   * - shape = "nationalflag.germany"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.germany"]; }

     - shape = "nationalflag.saudi_arabia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.saudi_arabia"]; }

   * - shape = "nationalflag.portugal"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.portugal"]; }

     - shape = "nationalflag.new_zealand"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.new_zealand"]; }

   * - shape = "nationalflag.cameroon"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.cameroon"]; }

     - shape = "nationalflag.bolivia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.bolivia"]; }

   * - shape = "nationalflag.tonga"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.tonga"]; }

     - shape = "nationalflag.croatia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.croatia"]; }

   * - shape = "nationalflag.south_sudan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.south_sudan"]; }

     - shape = "nationalflag.saint_kitts_and_nevis"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.saint_kitts_and_nevis"]; }

   * - shape = "nationalflag.haiti"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.haiti"]; }

     - shape = "nationalflag.afghanistan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.afghanistan"]; }

   * - shape = "nationalflag.suriname"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.suriname"]; }

     - shape = "nationalflag.abkhazia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.abkhazia"]; }

   * - shape = "nationalflag.togo"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.togo"]; }

     - shape = "nationalflag.macedonia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.macedonia"]; }

   * - shape = "nationalflag.algeria"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.algeria"]; }

     - shape = "nationalflag.mozambique"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.mozambique"]; }

   * - shape = "nationalflag.somaliland"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.somaliland"]; }

     - shape = "nationalflag.the_turkish_republic_of_northern_cyprus"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_turkish_republic_of_northern_cyprus"]; }

   * - shape = "nationalflag.andorra"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.andorra"]; }

     - shape = "nationalflag.south_africa"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.south_africa"]; }

   * - shape = "nationalflag.malta"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.malta"]; }

     - shape = "nationalflag.malawi"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.malawi"]; }

   * - shape = "nationalflag.namibia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.namibia"]; }

     - shape = "nationalflag.mali"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.mali"]; }

   * - shape = "nationalflag.iceland"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.iceland"]; }

     - shape = "nationalflag.nepal"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.nepal"]; }

   * - shape = "nationalflag.equatorial_guinea"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.equatorial_guinea"]; }

     - shape = "nationalflag.niger"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.niger"]; }

   * - shape = "nationalflag.the_philippines"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_philippines"]; }

     - shape = "nationalflag.nigeria"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.nigeria"]; }

   * - shape = "nationalflag.federated_states_of_micronesia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.federated_states_of_micronesia"]; }

     - shape = "nationalflag.bahrain"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.bahrain"]; }

   * - shape = "nationalflag.slovakia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.slovakia"]; }

     - shape = "nationalflag.antigua_and_barbuda"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.antigua_and_barbuda"]; }

   * - shape = "nationalflag.cambodia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.cambodia"]; }

     - shape = "nationalflag.denmark"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.denmark"]; }

   * - shape = "nationalflag.kenya"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.kenya"]; }

     - shape = "nationalflag.oman"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.oman"]; }

   * - shape = "nationalflag.israel"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.israel"]; }

     - shape = "nationalflag.brunei"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.brunei"]; }

   * - shape = "nationalflag.djibouti"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.djibouti"]; }

     - shape = "nationalflag.san_marino"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.san_marino"]; }

   * - shape = "nationalflag.singapore"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.singapore"]; }

     - shape = "nationalflag.costa_rica"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.costa_rica"]; }

   * - shape = "nationalflag.uganda"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.uganda"]; }

     - shape = "nationalflag.cote_d'ivoire"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.cote_d'ivoire"]; }

   * - shape = "nationalflag.colombia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.colombia"]; }

     - shape = "nationalflag.zimbabwe"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.zimbabwe"]; }

   * - shape = "nationalflag.the_people's_republic_of_china"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_people's_republic_of_china"]; }

     - shape = "nationalflag.sudan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.sudan"]; }

   * - shape = "nationalflag.north_korea"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.north_korea"]; }

     - shape = "nationalflag.luxembourg"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.luxembourg"]; }

   * - shape = "nationalflag.south_korea"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.south_korea"]; }

     - shape = "nationalflag.guinea"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.guinea"]; }

   * - shape = "nationalflag.the_marshall_islands"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_marshall_islands"]; }

     - shape = "nationalflag.malaysia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.malaysia"]; }

   * - shape = "nationalflag.romania"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.romania"]; }

     - shape = "nationalflag.benin"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.benin"]; }

   * - shape = "nationalflag.france"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.france"]; }

     - shape = "nationalflag.ethiopia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.ethiopia"]; }

   * - shape = "nationalflag.the_dominican_republic"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_dominican_republic"]; }

     - shape = "nationalflag.the_united_kingdom"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_united_kingdom"]; }

   * - shape = "nationalflag.the_central_african_republic"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_central_african_republic"]; }

     - shape = "nationalflag.palau"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.palau"]; }

   * - shape = "nationalflag.libya"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.libya"]; }

     - shape = "nationalflag.cape_verde"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.cape_verde"]; }

   * - shape = "nationalflag.papua_new_guinea"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.papua_new_guinea"]; }

     - shape = "nationalflag.serbia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.serbia"]; }

   * - shape = "nationalflag.montenegro"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.montenegro"]; }

     - shape = "nationalflag.the_solomon_islands"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_solomon_islands"]; }

   * - shape = "nationalflag.the_vatican_city"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_vatican_city"]; }

     - shape = "nationalflag.laos"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.laos"]; }

   * - shape = "nationalflag.tunisia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.tunisia"]; }

     - shape = "nationalflag.the_seychelles"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.the_seychelles"]; }

   * - shape = "nationalflag.turkmenistan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.turkmenistan"]; }

     - shape = "nationalflag.burundi"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.burundi"]; }

   * - shape = "nationalflag.bhutan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.bhutan"]; }

     - shape = "nationalflag.kyrgyzstan"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.kyrgyzstan"]; }

   * - shape = "nationalflag.ghana"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.ghana"]; }

     - shape = "nationalflag.saint_lucia"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.saint_lucia"]; }

   * - shape = "nationalflag.mauritania"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.mauritania"]; }

     - shape = "nationalflag.mauritius"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.mauritius"]; }

   * - shape = "nationalflag.yemen"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.yemen"]; }

     - shape = "nationalflag.norway"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.norway"]; }

   * - shape = "nationalflag.brazil"

       .. blockdiag::

          { A [label = "", shape = "nationalflag.brazil"]; }
     -
