https://freemarker.apache.org/docs/ref_builtins.html

model : Java Map
Grammar

- `${}` interpolation
  - `${str!"default str"}` (item.prop.prop)!
  - `obj??` => bool
  - 
- `<#-- -->` comment

- `<#` FTL tags
  - `<#if cond>` `<#elseif cond>` `<#else>` `<#if>`
  - list
    - `<#list list_var as item_var> ${item_var}`
    - `<#list list_var> <#items as item_var>`
    - `<#sep>,` `<#else>`
  - `<#include>`
  - <#ftl output_format="XML HTML">
  - `<#macro macro_name arg ..>`  user defined FTL Tag
    - `<#nested nested_expr, ..>`: yield
    - `<@macro_name arg_name=arg(; nested_var, ..)>`
  - `<#assign>` replace var
  - #local #global 
- built-ins
  - upper_case, cap_first, str?length, list?size
  - list_item?index, counter (1-baed index), item_parity => "odd", "even"
  - bool?string("a","b")
  - Item_cycle('a','b')
  - list?join(', ')
  - str?start_with(c) => bool 
  - list?filter(it -> it.prop) as item

Type

- scalar: str, num, bool, datae
- Container: hash, sequence, collection

variable

- (plain), #local, loop var, #global 

