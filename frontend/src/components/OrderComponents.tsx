// components/OrderPage.tsx
import * as React from "react";
import {
  Admin,
  Resource,
  List,
  Datagrid,
  TextField,
  EmailField,
  EditButton,
  DeleteButton,
  SimpleForm,
  Create,
  Edit,
  TextInput,
  Show,
  SimpleShowLayout,
  NumberInput,
  NumberField,
  required,
  SelectInput,
} from "react-admin";
import { orderStatusChoices, orderSourceChoices } from "../constants/enums";

export const OrderList = (props: any) => (
  <List {...props}>
    <Datagrid rowClick="show">
      <NumberField source="id" />
      <TextField source="customer_name" label="Customer Name" />
      <EmailField source="email_id" label="Email Id" />
      <TextField source="phone" />
      <TextField source="location" />
      <TextField source="service_requested" label="Service Requested" />
      <TextField source="order_details" label="Order Details" />
      <TextField source="status" />
      <TextField source="assigned_to" label="Assigned To" />
      <TextField source="source" />
      <EditButton />
      <DeleteButton />
    </Datagrid>
  </List>
);

export const OrderCreate = (props: any) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput
        source="customer_name"
        label="Customer Name"
        validate={required()}
      />
      <NumberInput
        source="email_id"
        label="Email Id"
        defaultValue={undefined}
      />
      <TextInput source="phone" defaultValue={undefined} />
      <TextInput source="location" defaultValue={undefined} />
      <TextInput
        source="service_requested"
        label="Service Requested"
        validate={required()}
      />
      <TextInput
        source="order_details"
        label="Order Details"
        defaultValue={undefined}
      />
      <TextInput
        source="assigned_to"
        label="Assigned To"
        defaultValue={undefined}
      />
      <SelectInput
        source="status"
        choices={orderStatusChoices}
        validate={required()}
        label="Status"
      />
      <SelectInput
        source="source"
        choices={orderSourceChoices}
        validate={required()}
        label="Source"
      />
    </SimpleForm>
  </Create>
);

export const OrderEdit = (props: any) => (
  <Edit {...props}>
    <SimpleForm>
      <TextInput
        source="customer_name"
        label="Customer Name"
        validate={required()}
      />
      <NumberInput
        source="email_id"
        label="Email Id"
        defaultValue={undefined}
      />
      <TextInput source="phone" defaultValue={undefined} />
      <TextInput source="location" defaultValue={undefined} />
      <TextInput
        source="service_requested"
        label="Service Requested"
        validate={required()}
      />
      <TextInput
        source="order_details"
        label="Order Details"
        defaultValue={undefined}
      />
      <TextInput
        source="assigned_to"
        label="Assigned To"
        defaultValue={undefined}
      />
      <SelectInput
        source="status"
        choices={orderStatusChoices}
        validate={required()}
        label="Status"
      />
      <SelectInput
        source="source"
        choices={orderSourceChoices}
        validate={required()}
        label="Source"
      />
    </SimpleForm>
  </Edit>
);

export const OrderShow = (props: any) => (
  <Show {...props}>
    <SimpleShowLayout>
      <NumberField source="id" />
      <TextField source="customer_name" label="Customer Name" />
      <TextField source="email_id" label="Email Id" />
      <TextField source="phone" />
      <TextField source="location" />
      <TextField source="service_requested" label="Service Requested" />
      <TextField source="order_details" label="Order Details" />
      <TextField source="assigned_to" label="Assigned To" />
      <TextField source="status" />
      <TextField source="source" />
    </SimpleShowLayout>
  </Show>
);
