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
  Show,
  SimpleShowLayout,
  TextInput,
  DateField,
  DateTimeInput,
  required,
} from "react-admin";

export const EmailList = (props: any) => (
  <List {...props}>
    <Datagrid rowClick="show">
      <TextField source="id" />
      <EmailField source="address" label="Sender Email" />
      <EmailField source="to" label="Recipient Email" />
      <TextField source="subject" />
      <TextField source="body" label="Body Preview" />
      <DateField source="sent_at" label="Sent At" />
      <TextField source="reply_to" label="Reply To" />
      <EditButton />
      <DeleteButton />
    </Datagrid>
  </List>
);

export const EmailCreate = (props: any) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="address" label="Sender Email" validate={required()} />
      <TextInput source="to" label="Recipient Email" validate={required()} />
      <TextInput source="subject" validate={required()} />
      <TextInput
        source="body"
        label="Email Body"
        multiline
        validate={required()}
      />
      <DateTimeInput
        source="sent_at"
        label="Sent At"
        defaultValue={new Date()}
      />
      <TextInput source="reply_to" label="Reply To" defaultValue={undefined} />
    </SimpleForm>
  </Create>
);

export const EmailEdit = (props: any) => (
  <Edit {...props}>
    <SimpleForm>
      <TextInput source="address" label="Sender Email" validate={required()} />
      <TextInput source="to" label="Recipient Email" validate={required()} />
      <TextInput source="subject" validate={required()} />
      <TextInput
        source="body"
        label="Email Body"
        multiline
        validate={required()}
      />
      <DateTimeInput source="sent_at" label="Sent At" />
      <TextInput source="reply_to" label="Reply To" defaultValue={undefined} />
    </SimpleForm>
  </Edit>
);

export const EmailShow = (props: any) => (
  <Show {...props}>
    <SimpleShowLayout>
      <TextField source="id" />
      <EmailField source="address" label="Sender Email" />
      <EmailField source="to" label="Recipient Email" />
      <TextField source="subject" />
      <TextField source="body" label="Email Body" />
      <DateField source="sent_at" label="Sent At" />
      <TextField source="reply_to" label="Reply To" />
    </SimpleShowLayout>
  </Show>
);
