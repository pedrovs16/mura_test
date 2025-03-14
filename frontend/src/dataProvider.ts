// dataProvider.ts
import simpleRestProvider from "ra-data-simple-rest";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

// Create the base provider using the API URL
const baseProvider = simpleRestProvider(API_URL);

const dataProvider = {
  ...baseProvider,
  getList: (resource: string, params: any) => {
    const { page, perPage } = params.pagination;
    const url = `${API_URL}/${resource}/?page=${page}&size=${perPage}`;

    return fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error(response.statusText);
        }
        return response.json();
      })
      .then((data) => {
        return {
          data: data.items,
          total: data.total,
        };
      });
  },
};

export default dataProvider;
