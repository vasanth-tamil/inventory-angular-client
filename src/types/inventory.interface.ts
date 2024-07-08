export interface InventoryInterface {
  ID?: number
  category: string
  date_added?: string
  item_name: string
  last_update?: string
  location: string | number
  quantity: string | number
  warning_limit: string | number
  supplier: string
  unit_price: string | number
}
