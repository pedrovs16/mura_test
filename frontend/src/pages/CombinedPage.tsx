// CombinedAdminPage.tsx
import React from "react";
import { Admin, Resource } from "react-admin";
import dataProvider from "../dataProvider";
import {
  OrderList,
  OrderCreate,
  OrderEdit,
  OrderShow,
} from "../components/OrderComponents";
import {
  EmailList,
  EmailCreate,
  EmailEdit,
  EmailShow,
} from "../components/EmailComponents";

const CombinedAdminPage = () => (
  <Admin dataProvider={dataProvider}>
    <Resource
      name="orders"
      list={OrderList}
      create={OrderCreate}
      edit={OrderEdit}
      show={OrderShow}
    />
    <Resource
      name="emails"
      list={EmailList}
      create={EmailCreate}
      edit={EmailEdit}
      show={EmailShow}
    />
  </Admin>
);

export default CombinedAdminPage;
