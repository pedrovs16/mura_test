// constants/enums.ts

export enum OrderStatus {
  PENDING = "Pending",
  IN_PROGRESS = "In Progress",
  COMPLETED = "Completed",
  CANCELED = "Canceled",
}

export const orderStatusChoices = [
  { id: OrderStatus.PENDING, name: "Pending" },
  { id: OrderStatus.IN_PROGRESS, name: "In Progress" },
  { id: OrderStatus.COMPLETED, name: "Completed" },
  { id: OrderStatus.CANCELED, name: "Canceled" },
];

export enum OrderSource {
  EMAIL = "Email",
  PHONE = "Phone",
  WEBSITE = "Website",
  MOBILE_APP = "Mobile App",
  OTHER = "Other",
}

export const orderSourceChoices = [
  { id: OrderSource.EMAIL, name: "Email" },
  { id: OrderSource.PHONE, name: "Phone" },
  { id: OrderSource.WEBSITE, name: "Website" },
  { id: OrderSource.MOBILE_APP, name: "Mobile App" },
  { id: OrderSource.OTHER, name: "Other" },
];
