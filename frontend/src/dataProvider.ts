// dataProvider.ts
import simpleRestProvider from "ra-data-simple-rest";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

// Create the base provider using the API URL
const baseProvider = simpleRestProvider(API_URL);

const dataProvider = {
  ...baseProvider,
  // Override getList to adapt FastAPI pagination (assumes response data is like: { items: [...], total: number, ... })
  getList: (resource: string, params: any) =>
    baseProvider.getList(resource, params).then((response) => {
      const { items, total } = response.data as unknown as {
        items: any[];
        total: number;
      };
      return {
        data: items,
        total: total,
      };
    }),
};

export default dataProvider;
